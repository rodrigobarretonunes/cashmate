from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 
import sqlite3

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


try:
    if DATABASE_URL.startswith("sqlite"):
        print("Usando SQLite:", DATABASE_URL)
        engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    else:
        print("Usando Postgres:", DATABASE_URL)
        engine = create_engine(DATABASE_URL)
except Exception as e:
    print("Erro ao conectar no banco:", e)
    raise


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()









