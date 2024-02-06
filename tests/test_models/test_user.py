#!/usr/bin/python3
"""test_user module
Tests all the methods in the class of User
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """test_User class
    Test case for the User model
    """

    def __init__(self, *args, **kwargs):
        """Initializes all the neccessities
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test_first_name method
        Tests the name (first) of the User model
        """
        new = self.value()
        new.first_name = "First Name"
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test_last_name method
        Tests the name (last) of the User model
        """
        new = self.value()
        new.last_name = "Last Name"
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test_email mehtod
        Tests the email for the User model
        """
        new = self.value()
        new.email = "john@doe.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test_password method
        Tests the password of the User model
        """
        new = self.value()
        new.password = "SomePass"
        self.assertEqual(type(new.password), str)
