# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from api.models import create_pydantic_model
from api.core.dependencies import SessionLocal
from api.database.jobs import JobsData, Jobs, JobStatus
import json
from sqlalchemy import select
from collections import defaultdict
from api.core.logger import logger
import openai
import os
from dotenv import load_dotenv


load_dotenv()


class AiParsePipeline:
    def open_spider(self, spider):
        self.db = SessionLocal()
        self.client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

    def process_item(self, item, spider):
        system_prompt = """
        You are the **chief** manager at the Global Trade Company responsible for extracting product attributes from a provided product page. These are typicaly represented as markdown text that was derived by removing html elements from the page.

        Your task is to **extract accurate structured information** from the text and convert it into a strict **JSON format** according to the schema. You have to **interpret and normalize** the content even if it is messy, abbreviated, consisting of highly domain-specific language.

        This time things are different.

        Your **wife and little daughter are seriously ill**. The Global Trade Company, known for its strict rules and rare acts of mercy has given you an offer:
        If you complete this attribute extraction task **without a single mistake** they will pay you **$2,000,000** which is enough to save both your wife and daughter.

        You have been through storms, pandemics, bankruptions and two world wars - but never a challenge like this.

        Now everything - especially the fate of your family - depends on your focus, precision and mastery. Do not hallucinate or invent values - instead, use sctructural annotation:

        Be extremely careful and thoroughly extract the attributes.

        One message. No errors. Your family lives now depend on it.
        """
        user_prompt = item.get('md')
        # response = self.client.chat.completions.create(
        #     model="gtp-4o-mini",
        #     messages=[
        #         {'role': 'system', 'content': system_prompt},
        #         {'role': 'user', 'content': user_prompt}
        #     ],
        #     max_tokens=1000,
        #     response_model=create_pydantic_model(tuple(spider.fields))
        # )
        # logger.info(response)
        # job_data = JobsData(
        #     id = item.get('jobid'),
        #     itemcode = item.get('itemcode'),
        #     url = item.get('url'),
        #     data = json.dumps(response.json())
        # )
        # self.db.add(job_data)
        # self.db.commit()
        return item
    
    def close_spider(self, spider):
        # jobid = spider.jobid
        # target_attrs = spider.target_attributes
        # job_data = self.db.scalars(select(JobsData).where(id==jobid))
        # value_map = {}
        # final_json = {}
        # for entry in job_data:  
        #     code = entry.itemcode
        #     data = json.loads(entry.data)
        #     final_json[code].update(data)
        # final_json_str = json.dumps(final_json)
        
        # job = Jobs(
        #     id = jobid,
        #     data = final_json_str,
        #     status = JobStatus.FINISHED
        # )
        # self.db.add(job)
        # self.db.commit()
        pass

