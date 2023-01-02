from typing import List

from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.models import UP
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, Integer, select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base
from .database import get_async_session


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    is_staff = Column(Boolean(), default=False, server_default="f", nullable=False)

    def __str__(self):
        return self.email

    def __repr__(self):
        return f"<User: {self.email}>"


class UserDatabase(SQLAlchemyUserDatabase):
    async def get_all_users(self) -> List[UP]:
        instances = await self.session.execute(select(self.user_table))
        return instances.scalars().all()


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    pass


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield UserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
