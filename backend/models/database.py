from typing import AsyncGenerator

import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from ..settings import Settings
from .base import Base

database_url = Settings().DATABASE_URL

metadata = sqlalchemy.MetaData()


engine = create_async_engine(
    database_url, pool_pre_ping=True, pool_size=75, max_overflow=25, future=True
)


async_session = sessionmaker(
    autoflush=True, bind=engine, class_=AsyncSession, future=True
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session.begin() as session:
        yield session


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
