#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Testing yhe City class..."""

from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_City(self):
        """All tests goes here"""
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))
        

if __name__ == '__main__':
    unittest.main()
