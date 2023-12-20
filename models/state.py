#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class
    Defines the state
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            return relationship(
                'City',
                back_populates='state',
                cascade='all,delete-orphan'
            )
        else:
            from models import storage
            all_cities = storage.all(City)
            state_cities = []
            for key, city in all_cities.items():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
