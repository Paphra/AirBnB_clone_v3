#!/usr/bin/python3
"""test_place module
Tests the Place model to see its operations
"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """test_Place class
    Inherits from test_basemodel to check all others things
    """

    def __init__(self, *args, **kwargs):
        """Initializes the neccessities
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test_city_id mehtod
        Tests the attached City ID
        """
        from models.city import City
        new = self.value()
        city = City()
        new.city_id = city.id
        new.save()

        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test_user_id method
        Tests the User ID attached
        """
        from models.user import User
        new = self.value()
        user = User()
        new.user_id = user.id
        new.save()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test_name
        Tests the name of the place
        """
        new = self.value()
        new.name = "My Place"
        new.save()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test_description mehtod
        Tests the description of the place
        """
        new = self.value()
        new.description = "Some Description"
        new.save()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test_number_rooms mehtod
        Tests the attached numbe of rooms for a place
        """
        new = self.value()
        new.number_rooms = 3
        new.save()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test_numner_bathrooms method
        Tests the number of bathrooms attached to a place
        """
        new = self.value()
        new.number_bathrooms = 5
        new.save()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test_max_guest mehtod
        Tests the maximum number of guests assigned to the place
        """
        new = self.value()
        new.max_guest = 5
        new.save()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test_price_by_night mehtod
        Tests the price by night set for the place
        """
        new = self.value()
        new.price_by_night = 500
        new.save()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test_latitude method
        Tests the latitude of the place
        """
        new = self.value()
        new.latitude = 3.493
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test_logitude method
        Tests the logitude of the place
        """
        new = self.value()
        new.latitude = 32.112
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test_amenity_ids method
        Tests the amenitites at the place
        """
        new = self.value()
        new.amenity_ids = []
        self.assertEqual(type(new.amenity_ids), list)
