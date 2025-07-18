from celery import Celery
from kombu import Queue
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


celery = Celery(
    __name__,
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
    broker_connection_retry_on_startup=True,

)

celery.conf.task_default_rate_limit = '500/m'

celery.autodiscover_tasks(["api.tasks"])

