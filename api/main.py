from api.database.deps import get_async_db
from api.database.models import Job, Task, Status
from api.core.utils import fetch_url, requires_js
from api.core.prompts import extract_attr_prompt, examples
from api.core.exceptions import OpenaiRequestError
from api.core.logger import logger
from api.models import JobResponse, create_extract_attr_model, ProductAttributeEntry, ProductAttributeList

from pathlib import Path
import os
import json
import uuid
import time
import re
from glob import glob
import pandas as pd
from fastapi import UploadFile, File, FastAPI, HTTPException, status, BackgroundTasks, Depends
from fastapi.responses import FileResponse, Response
from fuzzywuzzy import process
import uvicorn
from dotenv import load_dotenv
from typing import Optional, Any, Annotated
from pydantic import BaseModel, create_model
from sqlalchemy import update, select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import openai
import httpx
import random
from html_to_markdown import convert_to_markdown
import pathlib
import asyncio
import curl_cffi
from curl_cffi import requests
from api.tasks import create_item_enrichment_workflow
from celery import chain, chord, group
from api.worker.celery_app import celery
import io
import codecs
import sys
from urllib.parse import quote


load_dotenv()

INPUT_DIR = "./content/input"
OUTPUT_DIR = "./content/output"
PROJECT_ROOT = Path(__file__).parent.parent
PROXY_URLS = json.loads(os.getenv('PROXY_URLS'))
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = os.getenv('MODEL')
GOOGLE_CONCURRENCY_LIMIT = os.getenv('GOOGLE_CONCURRENCY_LIMIT')
SCRAPING_CONCURRENCY_LIMIT = os.getenv('SCRAPING_CONCURRENCY_LIMIT')
# ~~~~~~~~~~~~~ yandex creds ~~~~~~~~~~~~~~~~~~

YANDEX_FOLDERID = os.getenv('YANDEX_FOLDERID')
YANDEX_APIKEY = os.getenv('YANDEX_APIKEY')

YANDEX_CREDS = {'YANDEX_FOLDERID':YANDEX_FOLDERID, 'YANDEX_APIKEY':YANDEX_APIKEY}



app = FastAPI(
    title="Data enrichment api",
    description="API для заполнения csv файлов продуктов"
)



# def filter_response(response: ProductAttributeList, return_annotated: bool = False) -> ProductAttributeList:
#     if return_annotated:
#         filtered_entries = []
#         for entry in response['entries']:
#             filtered_entries.append(ProductAttributeEntry(
#                 attribute=entry['attribute']['value'],
#                 value=entry['value'],
#                 status=entry['attribute']['status'],
#                 explanation=entry['attribute']['explanation'] if 'explanation' in entry['attribute'] else "no explanation" # у модели pydantic может не быть поля explanation
#             ))
        
#         return ProductAttributeList(entries=filtered_entries)

#     filtered_entries = []
#     for entry in response['entries']:
#         if entry['attribute']['status'] == 'raw': # пропускаем нерелевантые аттрибуты пока что
#             continue

#         filtered_entries.append(ProductAttributeEntry(
#             attribute=entry['attribute']['value'],
#             value=entry['value']
#         ))
    
#     return ProductAttributeList(entries=filtered_entries)
        





def build_search_query(itemcode: str, supplier_name: str, full_product_name: str | None = None):
    query = f"{itemcode} {supplier_name}" if not full_product_name else f"{itemcode} {supplier_name} {full_product_name}"
    return query

@app.post('/api/v1/submit')
async def mock_submit_csv(
    db: Annotated[AsyncSession, Depends(get_async_db)],
    file: UploadFile = File(...)
):
    try:
        jobid = str(uuid.uuid4())
        filename = file.filename

        content = file.file
        df = pd.read_csv(content, encoding='utf-8')
        json_content = df.to_json(orient='columns', force_ascii=False)

        #проверка на дублирующиеся коды товара
        if df.loc[df['Код товара'].notna(), 'Код товара'].duplicated().sum() > 0:
            logger.exception(f"Обнаружены дубликаты в колонке Код товара! Отмена..")
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Дубликаты в колонке Код товара!")
        
        #проверка на наличие разных имен производителя в колонке
        if len(df.loc[df['Производитель'].notna(), 'Производитель'].unique()) > 1:
            logger.exception(f"Обнаружены разные производители в колонке Производитель! Отмена..")
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Разные производители в колонке Производитель!")
        
        
        threshold = 80
        image_cols = [col[0] for col in process.extract("Изображение", df.columns) if col[1] >= threshold]
        doc_cols = [col[0] for col in process.extract("Документация", df.columns) if col[1] >= threshold]
        item_codes = df.loc[df['Код товара'].notna() & df[image_cols].notna().any(axis=1) & df[doc_cols].notna().any(axis=1), 'Код товара']
        size_cols = [col[0] for col in process.extract("Размер", df.columns) if col[1] >= threshold]
        weight_cols = [col[0] for col in process.extract("Вес", df.columns) if col[1] >= threshold]
        target_attrs = [col for col in df.columns[df.columns.get_loc("Код товара")+1:].tolist() if col not in [*image_cols, *doc_cols, *weight_cols, *size_cols]]

        supplier = df.loc[df['Производитель'].notna(), 'Производитель'].unique()[0]

        job = Job(
            id=jobid,
            status=Status.PENDING,
            filename=filename,
            input_file_json=json_content
        )
        db.add(job)


        await db.flush()
        task_chains = []
        for itemcode in item_codes[:1]:
            row = Task(
                jobid=jobid,
                itemcode=itemcode
            )
            db.add(row)
            await db.flush()

            query = build_search_query(itemcode, supplier)

            chain = create_item_enrichment_workflow(
                row_id=row.id,
                query=query,
                n_links=5,
                yandex_creds=YANDEX_CREDS
            )
            task_chains.append(chain)
        
        await db.commit()

        celery_group = group(task_chains)
        result = celery_group.apply_async()

        job.status = Status.PROCESSING
        await db.commit()
        return jobid

    except Exception as e:
        await db.rollback()
        logger.exception(f"Unexpected error occured: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error occured: {str(e)}") from e
    
@app.get('/api/v1/load')
async def get_json(
    db: Annotated[AsyncSession, Depends(get_async_db)],
    job_id: str
):
    try:
        job = await db.scalar(select(Job).where(Job.id==job_id))
        filename = job.filename
        json_str = job.input_file_json
        # decoded_json_str = codecs.decode(json_str, 'unicode_escape')
        df = pd.read_json(json_str, orient='columns', encoding='utf-8')

        output = io.StringIO()
        df.to_csv(output, index=False, encoding='utf-8')
        csv_file = output.getvalue()


        safe_filename = quote(f"{filename}")
        return Response(
            content=csv_file,
            media_type='text/csv; charset=utf-8',
            headers={'Content-Disposition': f'attachment; filename="{safe_filename}"'}

        )
    except Exception as e:
        logger.exception(f"Unexpected error occured: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error occured: {str(e)}") from e 





@app.get('/api/v1/status/{job_id}')
async def get_job_status(
    job_id: str,
    db: Annotated[AsyncSession, Depends(get_async_db)]
):
    try:
        job = await db.scalar(select(Job).where(Job.id==job_id))
        job_status = job.status
        return JobResponse(
            id=job_id,
            status=job_status,
            message=f"queued task"
        )
    except Exception as e:
        logger.exception(f"Unexpected error occured: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error occured: {str(e)}") from e
    
