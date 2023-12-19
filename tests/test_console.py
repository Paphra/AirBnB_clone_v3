#!/usr/bin/python3
"""test_console module
Tests all the methods in the console module
"""
import os
import unittest
from io import StringIO
from models import storage
from console import HBNBCommand
from unittest.mock import patch


class test_console(unittest.TestCase):
    """Class to test the console methods
    """

    def test_help(self):
        """test_help method
        Testing the functioning of the do_help method of the console
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            self.assertEqual(f.readline(), '')
            self.assertTrue(f.getvalue().startswith('\nDocumented'))

    def test_all(self):
        """test_all method
        Tests the all feature
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all State')
            self.assertEqual(f.getvalue().strip(), '[]')
            HBNBCommand().onecmd('all Place')
            self.assertEqual(f.getvalue().strip(), '[]\n[]')

    def test_create(self):
        """test_create_method
        Tests the do_create(self, arg) method of the console
        """
        state_id = ''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Wakiso"')
            self.assertTrue(len(f.getvalue()) > 10)

            state_id = f.getvalue().strip()
            HBNBCommand().onecmd('show State {}'.format(state_id))
            line = f.getvalue().strip().split('\n')[1]
            self.assertNotEqual(line, '** no instance found **')
            self.assertTrue("'name': 'Wakiso'" in line)

            HBNBCommand().onecmd('show State {}'.format('Some-wierd-id'))
            line = f.getvalue().strip().split('\n')[2]
            self.assertEqual(line, '** no instance found **')

            HBNBCommand().onecmd('count State')
            line = f.getvalue().strip().split('\n')[3]
            self.assertEqual(line, '1')

            HBNBCommand().onecmd('all State')
            line = f.getvalue().strip().split('\n')[4]
            self.assertNotEqual(line, '[]')


if __name__ == '__main__':
    unittest.main()
