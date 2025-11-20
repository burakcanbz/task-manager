import os
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

env = os.getenv("ENVIRONMENT", "dev")

if env == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")
port = os.getenv("POSTGRES_PORT")
host = os.getenv("POSTGRES_HOST", "localhost")

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"

max_retries = 5
retry_delay = 2  

for attempt in range(max_retries):
    try:
        engine = create_engine(DATABASE_URL, echo=False)
        conn = engine.connect()
        conn.close()
        print("Database connection successful")
        break
    except OperationalError as e:
        print(f"Database connection failed ({attempt+1}/{max_retries}), retrying in {retry_delay}s...")
        time.sleep(retry_delay)
else:
    raise Exception("Database connection failed after multiple retries.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
