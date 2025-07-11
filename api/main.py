from core.dependencies import get_db
from core.utils import get_urls
from pathlib import Path
import os
import json
import uuid
from glob import glob
import pandas as pd
from core.logger import logger
from fastapi import UploadFile, File, FastAPI, HTTPException, status, BackgroundTasks, Depends
from fastapi.responses import FileResponse
from fuzzywuzzy import process as fuzzy_process
import uvicorn
from dotenv import load_dotenv
import subprocess
from typing import Optional, Any, Annotated
from pydantic import BaseModel, create_model
import sqlite3
from sqlalchemy.orm import Session
from scrapy.crawler import CrawlerProcess
import requests


load_dotenv()

INPUT_DIR = "./content/{jobid}/input"
OUTPUT_DIR = "./content/{jobid}/output"
PROJECT_ROOT = Path(__file__).parent.parent

def run_scrapy(
    item_codes, 
    item_supplier,
    jobid,
    target_attributes,
):
    cmd = [
        "scrapy",
        "crawl",
        "item_spider",
        "-a",
        f"item_codes={item_codes}",
        "-a",
        f"item_supplier={item_supplier}",
        "-a",
        f"jobid={jobid}",
        "-a",
        f"target_attributes={target_attributes}",
    ]


    process = subprocess.run(
        cmd,
        cwd=str(PROJECT_ROOT),
    )

app = FastAPI(
    title="Data enrichment api",
    description="API для заполнения csv файлов продуктов"
)


@app.post("/submit")
def submit_csv(
    bt: BackgroundTasks,
    db: Annotated[Session, Depends(get_db)],
    file: UploadFile = File(...)
    ) -> str:
    jobid = str(uuid.uuid4())
    job_input_dir = INPUT_DIR.format(jobid=jobid)
    job_output_dir = OUTPUT_DIR.format(jobid=jobid)

    if not os.path.exists(job_input_dir):
        os.makedirs(job_input_dir)
    if not os.path.exists(job_output_dir):
        os.makedirs(job_output_dir)

    df_path = os.path.join(job_input_dir, f"{file.filename}")

    content = file.file.read()
    with open(df_path, 'wb') as file:
        file.write(content)

    df = pd.read_csv(df_path)

    #проверка на дублирующиеся коды товара
    if df.loc[df['Код товара'].notna(), 'Код товара'].duplicated().sum() > 0:
        logger.exception(f"Обнаружены дубликаты в колонке Код товара! Отмена..")
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Дубликаты в колонке Код товара!")
    threshold = 80
    image_cols = [col[0] for col in fuzzy_process.extract("Изображение", df.columns) if col[1] >= threshold]
    doc_cols = [col[0] for col in fuzzy_process.extract("Документация", df.columns) if col[1] >= threshold]
    logger.debug(f"Обнаружены колонки изображений и документаций: {image_cols} {doc_cols}")
    item_codes = df.loc[df['Код товара'].notna() & df[image_cols].notna().any(axis=1) & df[doc_cols].notna().any(axis=1), 'Код товара']

    size_cols = [col[0] for col in fuzzy_process.extract("Размер", df.columns) if col[1] >= threshold]
    weight_cols = [col[0] for col in fuzzy_process.extract("Вес", df.columns) if col[1] >= threshold]
    target_attributes = [col for col in df.columns[df.columns.get_loc("Код товара")+1:].tolist() if col not in [*image_cols, *doc_cols, *weight_cols, *size_cols]]

    item_supplier = df.loc[df['Код товара'].notna(), 'Производитель'].values[0]


    for code in item_codes[:1]:
        urls = get_urls(
            f"{item_supplier} {code}",
            n_res=4,
            lang='ru'
        )
        for url in urls:
            params={
                "spider_name": "item_spider",
                "url": url
            }

            response = requests.get(
                url="http://localhost:9080/crawl.json",
                params=params,
                timeout=30
            )
            jobid = response





    # bt.add_task(
    #     run_scrapy,
    #     item_codes = item_codes, 
    #     item_supplier = item_supplier,
    #     jobid = jobid,
    #     target_attributes = target_attributes
    # )

    return jobid



# TODO проверить что паук запускается
    
if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, log_level="debug", reload=True)


