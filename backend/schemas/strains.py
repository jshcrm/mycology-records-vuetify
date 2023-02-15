from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class StrainCreate(BaseModel):
    name: str
    short_name: str
    notes: Optional[str]


class StrainDB(BaseModel):
    id: int
    name: str
    short_name: str
    notes: str

    class Config:
        orm_mode = True
