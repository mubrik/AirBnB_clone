#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Test case for the BaseModel class.
"""

from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import unittest




class TestBaseModelMethods(unittest.TestCase):
    """Test the methods of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Create object to use as test objects"""
        global b_obj1, b_obj2
        b_obj1 = BaseModel()
        b_obj2 = BaseModel()

    def test_str(self):
        """test the __str__ method"""
        assert_str = f"[BaseModel] ({b_obj1.id}) {b_obj1.__dict__}"
        self.assertEqual(assert_str, str(b_obj1))
        obj = BaseModel(**b_obj1.to_dict())
        obj.name = 'my first base object'
        obj.num = 1
        assert_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(assert_str, str(obj))

    def test_to_dict(self):
        """Test the to_dict method"""
        obj_dict = b_obj1.to_dict()
        self.assertEqual(obj_dict['id'], b_obj1.id)
        print(f"obj_dict['created_at'] = {obj_dict['created_at']}")
        print(f"b_obj1.created_at = {b_obj1.created_at}")
        self.assertEqual(obj_dict['created_at'], b_obj1.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], b_obj1.updated_at.isoformat())
        obj = BaseModel(**obj_dict)
        self.assertEqual(obj.to_dict(), b_obj1.to_dict())
        self.assertEqual(obj.to_dict(), obj_dict)
