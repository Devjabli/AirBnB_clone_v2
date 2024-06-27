#!/usr/bin/python3
"""State Module for HBNB project"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv

class State(BaseModel, Base):
    """State class"""
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City",
                              backref=backref("state", cascade='all'),
                              cascade="all, delete-orphan",
                              single_parent=True)

    if getenv("HBNB_TYPE_STORAGE") == "fs":
        @property
        def cities(self):
            """Return the list of City instances with state_id"""
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]
