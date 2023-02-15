from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import Base


class Spawn(Base):
    INOCULATION_TYPES = [
        "Spores",
        "Clone",
        "Grain",
        "Liquid Culture"
    ]

    id = Column(Integer, primary_key=True)

    identification = Column(String, default="")
    strain = Column(String, default="")

    # TODO: Should be choicefield of INOCULATION_TYPES
    inoculation_type = Column(String)
    inoculation_date = Column(DateTime(timezone=True))
    full_colonization_date = Column(DateTime(timezone=True))

    # children = relationship("Spawn", back_populates="children")

    # media_id = Column(Integer, ForeignKey("media.id"))
    # # media = relationship("Media", back_populates="spawns", uselist=False)
    # # # events = relationship("Event", back_populates="spawn")

    notes = Column(String, default="")
