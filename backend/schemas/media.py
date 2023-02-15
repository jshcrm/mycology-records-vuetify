from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, validator


class IngredientDB(BaseModel):
    id: int
    name: str
    amount: str
    measurement: str

    class Config:
        orm_mode = True



class MediaCreate(BaseModel):
    grow_id: int
    name: str
    inoculation_type: str
    inoculation_date: datetime
    full_colonization_date: Optional[datetime]
    notes: Optional[str]


class MediaDB(BaseModel):
    id: int
    name: str
    inoculation_type: str
    inoculation_date: datetime
    full_colonization_date: Optional[datetime]

    ingredients: List[IngredientDB]
    notes: str

    class Config:
        orm_mode = True
