from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.task_model import Task
from controller import task_controller
from utils.utils import seed_data #clean_tasks
from config.logger import logger
from exception.exception_handler import setup_exception_handlers
from config.db import Base, SessionLocal, engine

app = FastAPI(title="Task Manager API")

setup_exception_handlers(app)

@app.on_event("startup")
def on_start():
    logger.info("App starting...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if db.query(Task).count() == 0:
        seed_data()
    db.close()
    print("---App started successfully---")

@app.on_event("shutdown")
def on_shutdown():
    engine.dispose() 
    print("---App shutdown successfully---")

origins = [
    "http://localhost:5173",
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
