#!/usr/bin/python3
"""State Module for HBNB project"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv

dbBase = models.type_storage

class State(BaseModel, Base):
    """State class"""
    if dbBase == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref=backref("state", cascade='all'),
                              cascade="all, delete-orphan",
                              single_parent=True)
    else:
        name = ""
        
    if dbBase == "db":
        @property
        def cities(self):
            """Return the list of City instances with state_id"""
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]
