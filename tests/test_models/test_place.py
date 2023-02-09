
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Testing yhe Place class..."""

from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def test_Place(self):
        """All tests goes here"""
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))
