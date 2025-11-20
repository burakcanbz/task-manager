from sqlalchemy.orm import Session
from model.task_model import Task
import json
from config.db import get_db
from datetime import datetime

def clean_tasks():
    for db in get_db():
        try:
            deleted = db.query(Task).delete()
            db.commit()
            print(f"✅ {deleted} tasks deleted from DB")
        except Exception as e:
            db.rollback()
            print(f"❌ Error cleaning tasks: {e}")

def seed_data():
    try:
        with open("./data/tasks.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: tasks.json file not found!")
        return

    tasks_list = data["tasks"]

    for db in get_db():
        for t in tasks_list:
            existing_task = db.query(Task).filter(Task.id == t["id"]).first()
            if existing_task:
                print(f"Task with ID {t['id']} already exists, skipping...")
                continue

            task = Task(
                title=t["title"],
                description=t["description"],
                status=t["status"],
                priority=t["priority"],
                createdAt=datetime.fromtimestamp(t["createdAt"] / 1000),
                updatedAt=datetime.fromtimestamp(t["createdAt"] / 1000)
            )
            db.add(task)

        db.commit()
        print("✅ Seeder finished successfully!")
