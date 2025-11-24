import os
from redis.asyncio import Redis, ConnectionError
from utils.constants import redis_all_task_key
from config.logger import logger
from dotenv import load_dotenv
from config.config import REDIS_URL

REDIS_CLIENT = Redis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
