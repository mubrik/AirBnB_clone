#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Testing yhe State class..."""

from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Test the state class"""

    def test_State(self):
        """All tests goes here"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(hasattr(State, 'name'))


if __name__ == '__main__':
    unittest.main()
