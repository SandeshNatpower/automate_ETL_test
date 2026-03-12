from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2

from app.config import settings


def get_connection():
    return psycopg2.connect(settings.CONNSTR)


engine = create_engine(
    "postgresql+psycopg2://",
    creator=get_connection,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()