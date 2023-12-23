#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay
    Declares a class for the place model
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    user = relationship('User', back_populates='places')
    city = relationship('City', back_populates='places')

    @property
    def reviews(self):
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            return relationship(
                'Review',
                back_populates='review',
                cascade='all,delete-orphan'
            )

        from models import storage
        from models.review import Review

        all_reviews = storage.all(Review)
        place_reviews = []
        for key, review in all_reviews.items():
            if review.place_id == self.id:
                place_reviews.append(review)
        return place_reviews
