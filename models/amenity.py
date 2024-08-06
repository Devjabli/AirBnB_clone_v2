#!/usr/bin/python3
"""
Module Amenity class.
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """"Class that Define the Amenities"""
    if models.type_storage == 'db':
        __tablename__ = "amenities"
        name = Column(String(128),
                    nullable=False)
    else:
        name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)