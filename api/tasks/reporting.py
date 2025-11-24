from config.celery_config import celery_app
from celery.schedules import crontab
from config.logger import logger
from config.db import SyncSessionLocal
from repository.sync_repository import SyncTaskRepository
import datetime
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "tasks_report.txt")
os.makedirs(os.path.dirname(file_path), exist_ok=True)


@celery_app.task(name="generate_task_report", bind=True, max_retries=3)
def generate_task_report(self):
    logger.info("Scedular starting...")
    try:
        db = SyncSessionLocal()
        repo = SyncTaskRepository(db)
        logger.info("Database connected successfully.")

        min = 60
        tasks = repo.get_recent(minutes=min)
        if not tasks:
            logger.info(f"No tasks found in the last {min} minutes.")
            return

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(file_path, "a") as f:
                f.write(f"\n***** Report time: {now} *****\n")
                for t in tasks:
                    f.write(f"{t.id} - {t.title} - {t.createdAt}\n")
                f.flush()
            logger.info(f"{len(tasks)} task found. Report written to {file_path}")
        except IOError as e:
            logger.error(f"File write error: {e}")
            raise

    except Exception as e:
        logger.error(f"Error generating report: {e}", exc_info=True)
        self.retry(exc=e, countdown=5)
    finally:
        if db:
            db.close()

    logger.info("Report generation completed.")


celery_app.conf.beat_schedule = {
    "generate-report-every-20-minutes": {
        "task": "generate_task_report",
        "schedule": crontab(minute="*/20"),
    },
}
