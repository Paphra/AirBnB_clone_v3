#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity class
    For storing amenities in the system
    """
    name = ""
