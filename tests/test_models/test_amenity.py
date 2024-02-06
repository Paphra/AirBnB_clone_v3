#!/usr/bin/python3
"""test_amenity module
Contains a class that tests the amenity model
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """test_Amenity class
    Inherits from test_basemodel for testing the amenities
    """

    def __init__(self, *args, **kwargs):
        """Initializes the neccessities
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests the name of the amenity
        """
        new = self.value()
        new.name = "Some Name"
        self.assertEqual(type(new.name), str)
