#!/usr/bin/python3
"""test_state module
Tests the State model
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """test_state unittest
    Tests the State model
    """

    def __init__(self, *args, **kwargs):
        """Initializes the test module
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests the name type
        """
        new = self.value()
        new.name = "Some State"
        self.assertEqual(type(new.name), str)
