#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Testing the Amenity class"""

import os
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """setup"""
        self.id_regex = r"[\d\w]{8}-[\d\w]{4}-[\d\w]{4}-[\d\w]{4}-[\d\w]{12}"
        self.storage = storage
        self.storage.fpa = "test_amenity_db.json"
        if (os.path.isfile(self.storage.fpa)):
            os.remove(self.storage.fpa)
        storage.reload()

    def tearDown(self):
        """ teardown """
        if (os.path.isfile(self.storage.fpa)):
            os.remove(self.storage.fpa)
        del self.storage

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
        attr_name = f"{obj_data['__class__']}.{obj_data['id']}"
        self.assertEqual(self.storage.all()[f'{attr_name}'], new)
        self.assertIsInstance(new, Amenity)
        self.assertEqual(new.name, "tester")
        self.assertRegex(new.id, self.id_regex)


if __name__ == '__main__':
    unittest.main()
