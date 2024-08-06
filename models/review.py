#!/usr/bin/python3
"""
Module Review class.
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

dbBase = models.type_storage

class Review(BaseModel, Base):
    """This is the class for Review"""
    if dbBase == 'db':
        __tablename__ = 'reviews'

        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
