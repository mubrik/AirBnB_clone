#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Testing the Amenity class"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_Amenity(self):
        """All thest goes here"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(hasattr(Amenity, 'name'))


if __name__ == '__main__':
    unittest.main()
