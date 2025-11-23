from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.task_model import Task
from controller import task_controller
from utils.utils import check_database_connection, check_redis_connection, create_table, database_seeder #clean_tasks
from config.logger import logger
from exception.exception_handler import setup_exception_handlers
from config.db import engine
from config.logger import logger


app = FastAPI(title="Task Manager API")

setup_exception_handlers(app)

@app.on_event("startup")
async def on_start():
    await logger.info("App starting...")
    await check_database_connection()
    await check_redis_connection()
    await create_table()
    await database_seeder()

    await logger.info("---App started successfully---")

@app.on_event("shutdown")
async def on_shutdown():
    await engine.dispose() 
    await logger.info("---App shutdown successfully---")

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