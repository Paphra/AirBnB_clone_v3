#!/usr/bin/python3
""" City Module for HBNB project
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship(
        'Place',
        back_populates='city',
        cascade='all, delete-orphan'
    )

    @property
    def state(self):
        """state property
        The State in which the City belongs
        """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            return relationship('State', back_populates='cities')
        else:
            from models import storage
            from models.state import State
            all_states = storage.all(State)
            for key, state in all_states.items():
                if state.id == self.state_id:
                    return state
