#!/usr/bin/python3
"""test_base_model module
Tests the BaseModel model
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """test_basemodel class
    Contains methods that test the BaseModel model
    """

    def __init__(self, *args, **kwargs):
        """Initalizes the neccessary variables
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Setup method
        Sets up different items for testing
        """
        pass

    def tearDown(self):
        """tearDown method
        Tears down all the setup things
        """
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_default(self):
        """test_defaults
        Default settings for the tests to be done
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """test_kwargs
        Tests all the keyword arguments
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """test_kwargs_int method
        Tests the kwargs that are integers
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """test_save method
        Testing save method all the Base model
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """test_str method
        Tests the str method of the classes (models)
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """test_todict method
        Tests the method of to_dict for all models
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """test_kwards_none
        When the kwargs are none for a given model
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """test_kwargs_one method
        Tests what happens when there is only one kwwarg
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """test_id method
        Tests the generated id for each model
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test_created_at method
        The created_at property test
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """test_updated_at method
        The updated_at property test
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
