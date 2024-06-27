#!/usr/bin/python3

""" Representing the BaseModel class. """

import uuid
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """ Representing the BaseModel of the console project. """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __init__(self, *args, **kwargs):

        """
        Initializer of BaseModel

        Args:
            *args (Tuple): unused.
            **kwargs (dict): key and value of attributes.
        """

        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """
        Updating the attribute updated_at with current time 
        """
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        dictionary.pop('_sa_instance_state', None)

        return dictionary
    
    def delete(self):
        """ Deleting local instance from storage """
        models.storage.delete(self)
        
    def __str__(self):
        """
        Return the string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
