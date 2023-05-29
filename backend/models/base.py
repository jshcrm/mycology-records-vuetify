from pydantic import BaseModel
from typing import Dict, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Query

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


    @classmethod
    def objects(cls):
        return QueryManager(cls)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

        return self

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.flush()
        await session.refresh(self)
        return self

    async def delete(self, session: AsyncSession):
        await session.delete(self)
        await session.flush()
        return True


U = TypeVar("U", bound=BaseModel)


class QueryManager:
    def __init__(self, base_class: Base):
        self.base_class = base_class
        self.query: Query = select(self.base_class)

    def __str__(self):
        return f"<{self.__class__.__name__}: {str(self.__class__.__name__)}>"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {str(self)}>"

    def filter(self, **kwargs) -> Base:
        self.query = self.query.where(*[self.base_class.__table__.c[key] == value for (key, value) in kwargs.items()])
        return self

    async def first(self, session: AsyncSession):
        result = await session.execute(self.query)
        return result.scalars().first()

    async def all(self, session: AsyncSession):
        result = await session.execute(self.query)
        return result.scalars().all()

    def create(self, instance: U, **kwargs) -> Base:
        instance_data = instance.dict()
        instance = self.base_class(**instance_data, **kwargs)
        return instance

    def create_from_dict(self, **kwargs) -> Base:
        instance = self.base_class(**kwargs)
        return instance
