import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from config.config import (
    DATABASE_URL,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PORT,
    SYNC_DATABASE_URL,
)

max_retries = 5
retry_delay = 2
engine = None

engine = create_async_engine(
    DATABASE_URL, echo=False, pool_size=10, max_overflow=10, pool_timeout=15
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)

Base = declarative_base()


async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    except Exception as e:
        await db.close()
        raise e
    finally:
        await db.close()


sync_engine = create_engine(SYNC_DATABASE_URL, pool_size=10, max_overflow=10)
SyncSessionLocal = sessionmaker(bind=sync_engine, autocommit=False, autoflush=False)
