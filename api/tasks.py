from celery import shared_task, group, chain, chord
from celery.exceptions import Ignore
import time
from celery.utils.log import get_task_logger
from limits import RateLimitItemPerSecond, RateLimitItemPerMinute
from limits.storage import RedisStorage
from limits.strategies import MovingWindowRateLimiter
import os
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from api.database.models import Task, Job
from api.yandex_client.yandex import YandexSearchAPIKeyClient, AsyncYandexSearchAPIKeyClient
from yandex_search_api import SearchType
import json
from contextlib import contextmanager
import asyncio
from curl_cffi import requests
from html_to_markdown import convert_to_markdown
from api.core.prompts import extract_characterstics_section_prompt, extract_characterstics_examples
from api.core.utils import requires_js
from api.models import ProductCharacteristicsSectionList
import openai
import httpx
import re
from playwright.sync_api import sync_playwright

# ~~~~~~~~~~~~~ DB session ~~~~~~~~~~~~~~~~~~~~~

sync_db_url = os.getenv("DATABASE_URL")
engine = create_engine(
    sync_db_url
)
session = sessionmaker(
    bind=engine
)

@contextmanager
def get_sync_db():
    with session() as s:
        yield s


# ~~~~~~~~~~~~~ RATE LIMIT ~~~~~~~~~~~~~~~~~~~~~

storage = RedisStorage("redis://redis:6379/1")

limiter = MovingWindowRateLimiter(storage)

YANDEX_SEARCH_API_LIMIT = RateLimitItemPerSecond(2)

# ~~~~~~~~~~~~~~ OPENAI CREDS ~~~~~~~~~~~~~~~~~~

OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
OPENAI_PROXY = os.getenv("OPENAI_PROXY")

class RateLimitExceedError(Exception):
    pass


logger = get_task_logger(__name__)

def create_item_enrichment_workflow(row_id, query, n_links, yandex_creds):
    return chain(
        get_urls.s(row_id, query, n_links, yandex_creds),
        scrape_all.s(row_id),
        extract_sections.s(row_id)
        # chord(group(extract_sections.s(row_id)), extract_attributes.s(row_id))
    )

def fetch_url(url: str, proxy: str = None) -> str:
    with requests.Session() as s:
        response = s.get(
            url,
            proxy=proxy, 
            impersonate='chrome136',
            timeout=30
        )

        return response.text
    
def fetch_url_playwright(url: str) -> str:
    with sync_playwright() as p:
        logger.info(f"Starting playwright in headless mode to scrape {url}")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until='networkidle')
        html = page.content()
        browser.close()
        logger.info(f"Closing playwright browser and returning html...")
        return html




@shared_task(bind=True)
def get_urls(self, row_id, query, n_links, yandex_creds):
    try:
        if not limiter.test(YANDEX_SEARCH_API_LIMIT, "yandex_search"):
            raise RateLimitExceedError(f"rate limit exceeded")
        limiter.hit(YANDEX_SEARCH_API_LIMIT, "yandex_search")
        # get_yandex_links("query")
        logger.info(f'TASK {self.request.id} Called Api')
        async def call_yandex():
            async with AsyncYandexSearchAPIKeyClient(folder_id=yandex_creds['YANDEX_FOLDERID'], api_key=yandex_creds['YANDEX_APIKEY']) as client:
                return await client.get_links(
                    query_text=query,
                    search_type=SearchType.RUSSIAN,
                    n_links=n_links
                )
        
        links = asyncio.run(call_yandex()) # блокирует поток также как и синхронный клиент, зато дешевле :)

        with get_sync_db() as db:
            db.execute(update(Task).where(Task.id==row_id).values(urls=json.dumps(links)))
            db.commit()

        return links
    
    except RateLimitExceedError as e:
        logger.warning(f"TASK {self.request.id} WAS RATE LIMITED")
        raise self.retry(countdown=3, max_retries=3)
    except Exception as e:
        logger.warning(f"Exception occured during executing task 'get_urls' {self.request.id}: {str(e)}")
        raise


@shared_task(bind=True)
def scrape_url(self, url) -> tuple[str]:
    try:
        logger.info(f"Scraping {url}...")
        html = fetch_url(url)
        if requires_js(html):
            logger.warning(f"Webpage {url} requires js, attempting to scrape with playwright...")
            html = fetch_url_playwright(url)
        logger.info(f"Finished scraping {url}")
        return html
    except Exception as e:
        logger.warning(f"Exception occured during executing task 'scrape_url' {self.request.id}: {str(e)}")
        raise

@shared_task(bind=True)
def process_scraped_results(self, htmls, row_id) -> list[str]:
    try:
        markdowns = [re.sub(r'\n{3,}', '\n\n', convert_to_markdown(html).strip()) for html in htmls]
        
        scraped_data_str = json.dumps(markdowns, ensure_ascii=False)
        with get_sync_db() as db:
            db.execute(update(Task).where(Task.id==row_id).values(scraped_data=scraped_data_str))
            db.commit()
        return markdowns
    except Exception as e:
        logger.warning(f"Exception occured during executing task 'process_scraped_results' {self.request.id}: {str(e)}")
        raise

@shared_task(bind=True)
def scrape_all(self, urls, row_id):
    logger.info(f"Launching scraping chord...")
    return chord(
        group(scrape_url.s(url) for url in urls),
        process_scraped_results.s(row_id)
    )()


@shared_task(bind=True)
def extract_sections(self, markdowns, row_id) -> str:
    try:
        openai_client = openai.OpenAI(
            api_key=OPENAI_APIKEY,
            http_client=httpx.Client(proxy=OPENAI_PROXY)
        )

        validation_model = ProductCharacteristicsSectionList
        json_schema = validation_model().model_dump_json()

        merged_markdown = f"\n\n\n{'~'*25}\n\n\n".join(markdowns)

        prompt = extract_characterstics_section_prompt.format(json_schema, extract_characterstics_examples, merged_markdown)
        resp = openai_client.chat.completions.parse(
            model="gpt-4.1-mini",
            messages=[
                {'role': 'system', 'content': prompt},
            ],
            timeout=60,
            response_format=validation_model
        ),

        resp_json = resp[0].choices[0].message.content

        with get_sync_db() as db:
            db.execute(update(Task).where(Task.id==row_id).values(extracted_sections=resp_json, prompt=prompt))
            db.commit()
        return resp_json
    except Exception as e:
        logger.warning(f"Exception occured during executing task 'extract_sections' {self.request.id}: {str(e)}")
        raise

@shared_task(bind=True)
def extract_attributes(self, sections, row_id) -> list[str]:
    try:

        # merged_sections = 

        openai_client = openai.OpenAI(
            api_key=OPENAI_APIKEY,
            http_client=httpx.Client(proxy=OPENAI_PROXY)
        )

        validation_model = ProductCharacteristicsSectionList
        json_schema = validation_model().model_dump_json()

        prompt = extract_characterstics_section_prompt.format(json_schema, extract_characterstics_examples, ...)
        resp = openai_client.chat.completions.parse(
            model="gpt-4.1-mini",
            messages=[
                {'role': 'system', 'content': prompt},
            ],
            timeout=60,
            response_format=validation_model
        ),

        resp_json = resp[0].choices[0].message.content

        with get_sync_db() as db:
            db.execute(update(Task).where(Task.id==row_id).values(openai_response=resp_json))
            db.commit()
        return resp_json
    except Exception as e:
        logger.warning(f"Exception occured during executing task 'extract_attributes' {self.request.id}: {str(e)}")
        raise

def finalize_csv(job_id):
    pass