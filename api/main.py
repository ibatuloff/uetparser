from core.dependencies import get_db
from core.utils import get_urls, fetch_url, requires_js, system_prompt, examples
from core.logger import logger
from models import create_pydantic_model

from pathlib import Path
import os
import json
import uuid
from glob import glob
import pandas as pd
from fastapi import UploadFile, File, FastAPI, HTTPException, status, BackgroundTasks, Depends
from fastapi.responses import FileResponse
from fuzzywuzzy import process
import uvicorn
from dotenv import load_dotenv
from typing import Optional, Any, Annotated
from pydantic import BaseModel, create_model
from sqlalchemy.orm import Session
import openai
import httpx
import random
from html_to_markdown import convert_to_markdown


load_dotenv()

INPUT_DIR = "/content/input"
OUTPUT_DIR = "/content/output"
PROJECT_ROOT = Path(__file__).parent.parent
PROXY_URLS = json.loads(os.getenv('PROXY_URLS'))
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = os.getenv('MODEL')


app = FastAPI(
    title="Data enrichment api",
    description="API для заполнения csv файлов продуктов"
)

def get_proxy() -> str:
    return random.choice(PROXY_URLS)


@app.post("/submit")
def submit_csv(
    db: Annotated[Session, Depends(get_db)],
    file: UploadFile = File(...)
    ) -> str:
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df_path = os.path.join(INPUT_DIR, f"{file.filename}")

    content = file.file.read()
    with open(df_path, 'wb') as file:
        file.write(content)

    df = pd.read_csv(df_path)

    #проверка на дублирующиеся коды товара
    if df.loc[df['Код товара'].notna(), 'Код товара'].duplicated().sum() > 0:
        logger.exception(f"Обнаружены дубликаты в колонке Код товара! Отмена..")
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Дубликаты в колонке Код товара!")
    threshold = 80
    image_cols = [col[0] for col in process.extract("Изображение", df.columns) if col[1] >= threshold]
    doc_cols = [col[0] for col in process.extract("Документация", df.columns) if col[1] >= threshold]
    item_codes = df.loc[df['Код товара'].notna() & df[image_cols].notna().any(axis=1) & df[doc_cols].notna().any(axis=1), 'Код товара']
    size_cols = [col[0] for col in process.extract("Размер", df.columns) if col[1] >= threshold]
    weight_cols = [col[0] for col in process.extract("Вес", df.columns) if col[1] >= threshold]
    target_attributes = [col for col in df.columns[df.columns.get_loc("Код товара")+1:].tolist() if col not in [*image_cols, *doc_cols, *weight_cols, *size_cols]]

    supplier = df.loc[df['Производитель'].notna(), 'Производитель'].unique()[0]
    item_codes = df.loc[df['Код товара'].notna(), 'Код товара'].values

    _, validation_model = create_pydantic_model(tuple(target_attributes))
    json_schema = validation_model.model_json_schema()

    result = {}
    
    texts = []
    for i, code in enumerate(item_codes[:2]):
        logger.info(f"processing code {code} supplier {supplier}")
        urls = get_urls(query=f"{supplier} {code}", proxy=random.choice(PROXY_URLS), n_res=2)
        logger.info(f"fetched {len(urls)} urls: {urls}")
        html_texts = []
        texts = []
        for url in urls:
            html = fetch_url(url, proxy=random.choice(PROXY_URLS))
            text = convert_to_markdown(html)
            if requires_js(text):
                pass # TODO добавить fallback 
            html_texts.append((html))
            texts.append((text))
        # сохранить код страниц для дебага
        with open(f'content\output\index_{i}.html', 'w', encoding='utf-8') as html_file, open(f'content\output\markdown_{i}', 'w', encoding='utf-8') as md_file:
            for i, scraped_data in enumerate(zip(html_texts, texts)):
                html_file.write(scraped_data[0])
                md_file.write(scraped_data[1])
                logger.info(f"saved ")

        merged_text = '\n\n\n\n\n'.join(texts)
        openai_proxy = get_proxy()
        openai_client = openai.OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            http_client=httpx.Client(proxy='http://'+openai_proxy)
        )
        resp = openai_client.chat.completions.parse(
            model=MODEL,
            messages=[
                {'role': 'system', 'content': system_prompt.format(json_schema=json_schema, examples=examples, md=merged_text)},
            ],
            response_format=validation_model
        )
        resp = resp.choices[0].message.content

        json_dir = 'content/output/responses'
        os.makedirs(json_dir, exist_ok=True)
        with open(os.path.join(json_dir, f'response_{code}_merged_urls.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(resp, indent=2, ensure_ascii=False))

        result[code] = resp



    return result




    
if __name__=="__main__":
    # print(get_proxy())
    # print(proxy_dict)
    # print(PROXY_URLS)
    uvicorn.run("main:app", host="0.0.0.0", port=8888, log_level="debug", reload=True)


