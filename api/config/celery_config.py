import os
from celery import Celery
from dotenv import load_dotenv
from config.config import REDIS_URL


def create_celery():

    celery_app = Celery(
        "worker", broker=REDIS_URL, backend=REDIS_URL, include=["tasks.reporting"]
    )

    celery_app.conf.update(
        task_serializer="json",  # use json for task serialization
        accept_content=["json"],  # accept json for task deserialization
        result_serializer="json",  # use json for result serialization
        timezone="Europe/Istanbul",  # use istanbul time
        enable_utc=True,  # use utc time
        task_track_started=True,  # track task start time
        task_time_limit=5 * 60,  # kill task if it takes longer than 5 minutes
        task_soft_time_limit=3 * 60,  # soft kill task if it takes longer than 3 minutes
        worker_prefetch_multiplier=1,  # prefetch 1 task at a time
    )

    return celery_app


celery_app = create_celery()
