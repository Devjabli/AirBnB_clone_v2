#!/usr/bin/python3

""" Representing the BaseModel class. """

from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy import Column, DateTime, String


if models.type_storage == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """ Representing the BaseModel of the console project. """
    if models.type_storage == 'db':
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
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """
        Updating the attribute updated_at with current time 
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        
        list_key = ["created_at", "updated_at"]
        for k in list_key:
            if k in dictionary:
                dictionary[k] = dictionary[k].strftime('%Y-%m-%dT%H:%M:%S.%f')
        dictionary["__class__"] = self.__class__.__name__
        
        return dictionary
    
    def delete(self):
        """ Deleting local instance from storage """
        models.storage.delete(self)
        
    def __str__(self):
        """
        Return the string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
