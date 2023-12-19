#!/usr/bin/python3
"""test_city module
For testing the City model
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """test_City class
    For testing the City model
    """

    def __init__(self, *args, **kwargs):
        """Initializes all the neccessities
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests the state_id that has been assigned
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Tests the name of the City
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
