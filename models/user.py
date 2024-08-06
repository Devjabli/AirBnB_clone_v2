#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
from models.place import Place

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

dbBase = models.type_storage

class User(BaseModel, Base):
    """This is the class user"""
    if dbBase == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship("Place",
                            backref="user",
                            cascade='all',
                            passive_deletes=True)
        reviews = relationship("Review", backref="user",
                            cascade="delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)