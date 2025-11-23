import os
from redis.asyncio import Redis, ConnectionError
from utils.constants import redis_all_task_key
from config.logger import logger
from dotenv import load_dotenv


env = os.getenv("ENVIRONMENT", "dev")

if env == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

if REDIS_PASSWORD:
    REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"
else:
    REDIS_URL = f"redis://{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"

REDIS_CLIENT = Redis.from_url(
    REDIS_URL,
    encoding="utf-8",
    decode_responses=True
)