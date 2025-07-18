from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, sessionmaker
import json
import os
from functools import partial





async_db_url = "postgresql+asyncpg://admin:admin@db:5432/parser_db"


engine = create_async_engine(
    async_db_url
)
session = async_sessionmaker(
    bind=engine
)
async def get_async_db():
    async with session() as s:
        yield s



