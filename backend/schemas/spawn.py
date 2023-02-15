from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class SpawnCreate(BaseModel):
    strain: str
    inoculation_type: str
    inoculation_date: Optional[datetime]
    full_colonization_date: Optional[datetime]
    notes: Optional[str]


class SpawnDB(BaseModel):
    id: int
    strain: str
    inoculation_type: str
    inoculation_date: Optional[datetime]
    full_colonization_date: Optional[datetime]
    notes: Optional[str]

    class Config:
        orm_mode = True
