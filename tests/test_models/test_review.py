#!/usr/bin/python3
"""test_review module
Contains the TestCase for testing the Reveiew model
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_Review(test_basemodel):
    """test_Review class
    Tests the Review model"""

    def __init__(self, *args, **kwargs):
        """Initializes all the neccessary items
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test_place_id method
        Tests the place Id attached to the review
        """
        from models.place import Place
        new = self.value()
        place = Place()
        new.place_id = place.id
        new.save()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test_user_id method
        Tests the User id attached to the review
        """
        from models.user import User
        new = self.value()
        user = User()
        new.user_id = user.id
        new.save()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test_text method
        Tests the review text
        """
        new = self.value()
        new.text = "Some text"
        self.assertEqual(type(new.text), str)
