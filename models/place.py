#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False),
)


class Place(BaseModel, Base):
    """ A place to stay
    Declares a class for the place model
    """
    __tablename__ = 'places'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    city = relationship('City', back_populates='places')
    user = relationship('User', back_populates='places')

    @property
    def amenities(self):
        """Returns the amenities
        """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            return relationship(
                'Amenity',
                secondary=place_amenity,
                backref='place_amenities',
                viewonly=False
            )
        from models.amenity import Amenity
        all_amenities = models.storage.all(Amenity)
        filtered = []
        for amenity in all_amenities:
            if amenity.id in self.amenity_ids:
                filtered.append(amenity)

        return filtered

    @amenities.setter
    def amenities(self, amenity):
        """Adds an amenity id
        """
        from models.amenity import Amenity
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)

    @property
    def reviews(self):
        """Returns the reviews
        """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            return relationship(
                'Review',
                back_populates='review',
                cascade='all,delete-orphan'
            )

        from models.review import Review

        all_reviews = models.storage.all(Review)
        place_reviews = []
        for key, review in all_reviews.items():
            if review.place_id == self.id:
                place_reviews.append(review)
        return place_reviews
