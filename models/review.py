#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information
    """
    __tablename__ = 'reviews'
    __table_args__ = ({'extend_existing': True})
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='reviews')

    @property
    def place(self):
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            return relationship('Place', back_populates='reviews')

        from models import storage
        from models.place import Place
        all_places = storage.all(Place)
        for key, place in all_places.items():
            if place.id == self.place_id:
                return place
