from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    __abstract__ = True

SQLITE_URL = "sqlite:///../parser.db"

engine = create_engine(SQLITE_URL)

SessionLocal = sessionmaker(bind=engine)