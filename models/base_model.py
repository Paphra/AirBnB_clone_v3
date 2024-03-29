#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    __abstract__ = True

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        for key, value in kwargs.items():
            if key != '__class__':
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            {key: value for key,
                value in self.__dict__.items() if key != '_sa_instance_state'}
        )

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        ret = {}       # dictionary to return
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if key in ['created_at', 'updated_at']:
                    ret[key] = datetime.isoformat(value)
                else:
                    ret[key] = value
        ret['__class__'] = self.__class__.__name__
        return ret

    def delete(self):
        """delete method
        Deletes the current instance from the storage
        """
        models.storage.delete(self)
