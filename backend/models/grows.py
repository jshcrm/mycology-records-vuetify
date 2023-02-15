from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship

from backend.models.base import Base
from backend.models.strains import Strain
from backend.models.media import Media


class Grow(Base):
    id = Column(Integer, primary_key=True)

    strain_id = Column(Integer, ForeignKey("strain.id"))
    strain = relationship("Strain", back_populates="grows", lazy="selectin", uselist=False)

    medias = relationship("Media", back_populates="grow", lazy="selectin", order_by="Media.inoculation_date")
