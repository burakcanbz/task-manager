from sqlalchemy.orm import Session
from model.task_model import Task
from sqlalchemy import select
from datetime import datetime, timedelta, timezone


class SyncTaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_recent(self, minutes: int):
        tz = timezone(timedelta(hours=3))
        threshold = datetime.now(tz) - timedelta(minutes=minutes)
        s = select(Task).where(Task.createdAt >= threshold)
        return self.session.scalars(s).all()
