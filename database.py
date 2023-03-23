from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_URL

DATABASE_URL = DB_URL

db_engine = create_engine(DATABASE_URL, echo = False,  pool_pre_ping=True)
SessionLocal = sessionmaker(bind=db_engine)

Base = declarative_base()

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()