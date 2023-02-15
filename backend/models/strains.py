from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import Base


class Strain(Base):
    id = Column(Integer, primary_key=True)

    name = Column(String)
    short_name = Column(String(3))

    notes = Column(String, default="")

    grows = relationship("Grow", back_populates="strain")
