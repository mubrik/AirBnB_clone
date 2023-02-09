#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""testing the User class..."""

import unittest
# decided to import directly not through exports
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class"""

    def test_User(self):
        """All tests goes here"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertTrue(hasattr(User, 'password'))
        

if __name__ == '__main__':
    unittest.main()
