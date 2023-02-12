#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Testing the Review class..."""

from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def test_Review(self):
        """All tests goes here"""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(hasattr(Review, 'text'))
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
