from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from backend.models.base import Base


class Ingredient(Base):
    MEASUREMENTS = [
        "grams",
        "parts"
    ]

    id = Column(Integer, primary_key=True)

    media_id = Column(Integer, ForeignKey("media.id"))
    media = relationship("Media", back_populates="ingredients", uselist=False)

    name = Column(String, default="")
    amount = Column(Numeric)

    # TODO: Should be choicefield of MEASUREMENTS
    measurement = Column(String, default="")


class Media(Base):
    TYPES = [
        "Agar",
        "Grain",
        "Liquid Culture"
    ]

    id = Column(Integer, primary_key=True)

    grow_id = Column(Integer, ForeignKey("grow.id"))
    grow = relationship("Grow", back_populates="medias", lazy="selectin", uselist=False)

    inoculation_type = Column(String)
    inoculation_date = Column(DateTime(timezone=True))
    full_colonization_date = Column(DateTime(timezone=True))

    ingredients = relationship("Ingredient", lazy="selectin", back_populates="media")

    name = Column(String)
    notes = Column(String, default="")
