from typing import List

from pydantic import BaseModel

from backend.schemas.media import MediaDB
from backend.schemas.strains import StrainDB


class GrowCreate(BaseModel):
    strain_id: int


class GrowDB(BaseModel):
    id: int
    strain_id: int
    strain: StrainDB
    medias: List[MediaDB]

    class Config:
        orm_mode = True
