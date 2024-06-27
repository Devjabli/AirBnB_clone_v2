#!/usr/bin/python3
"""
Module City class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """ City class,  state ID and name
    Attributes:
        name: input name
        state id: input id
    """

    __tablename__ = "cities"

    name = Column(String(128),
                  nullable=False)
    state_id = Column(String(60),
                      ForeignKey('states.id'))
    places = relationship("Place",
                          backref=backref("cities", cascade='all'),
                          cascade="all")