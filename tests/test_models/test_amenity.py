#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Testing the Amenity class"""

import os
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """setup"""
        self.id_regex = r"[\d\w]{8}-[\d\w]{4}-[\d\w]{4}-[\d\w]{4}-[\d\w]{12}"

    def test_Amenity(self):
        """All thest goes here"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_new_amenity(self):
        """test a new instance"""
        new = Amenity()
        new.name = "tester"
        new.save()
        obj_data = new.to_dict()
        copy = Amenity(**obj_data)
        attr_name = f"{obj_data['__class__']}.{obj_data['id']}"
        self.assertEqual(storage.all()[f'{attr_name}'], new)
        self.assertIsInstance(new, Amenity)
        self.assertEqual(new.name, "tester")
        self.assertEqual(new.name, copy.name)
        self.assertEqual(new.id, copy.id)
        self.assertRegex(new.id, self.id_regex)


class TestAmenityAttributes(unittest.TestCase):
    """Test case for Amenity attributes"""

    def setUp(self):
        """setup models for every test method"""
        self.ins = Amenity()

    def tearDown(self):
        """teardown for every test method, can implement teardown later"""
        pass

    def test_id(self):
        """Tests the id attribute"""
        self.assertTrue(hasattr(self.ins, "id"))
        self.assertEqual(type(self.ins.id), str)

    def test_created_at(self):
        """Tests the created_at attribute"""
        self.assertTrue(hasattr(self.ins, "created_at"))
        self.assertEqual(type(self.ins.created_at), datetime)
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)

    def test_updated_at(self):
        """Tests the updated_at attribute"""
        self.assertTrue(hasattr(self.ins, "updated_at"))
        self.assertEqual(type(self.ins.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()
