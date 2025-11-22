from config.db import Base, engine

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.task_model import Task
from controller import task_controller
from utils.utils import seed_data #clean_tasks
from exception.exception_handler import setup_exception_handlers
from config.db import SessionLocal

app = FastAPI(title="Task Manager API")

setup_exception_handlers(app)

Base.metadata.create_all(bind=engine)

db = SessionLocal()
if db.query(Task).count() == 0:
    seed_data()
db.close()

origins = [
    "http://localhost:5173", # Change port to vite default port  
    "http://127.0.0.1:5713",
    "*", # Allow all origins
]

# Enable credentials from coming requests.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(task_controller.router)
