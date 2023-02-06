#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Test case for the BaseModel class.
"""

from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import unittest


class TestBaseModelAttributes(unittest.TestCase):
    """Test case for BaseModel attributes"""

    @classmethod
    def setUpClass(self):
        """Create object to use as test objects"""
        global b_obj1, b_obj2
        b_obj1 = BaseModel()
        b_obj2 = BaseModel()

    def test_id(self):
        """Tests the id attribute"""
        self.assertTrue(hasattr(b_obj1, 'id'))
        self.assertEqual(type(b_obj1.id), str)
        self.assertNotEqual(b_obj1.id, b_obj2.id)

        def test_created_at(self):
            """Tests the created_at attribute"""
            self.assertTrue(hasattr(b_obj1, 'created_at'))
            self.assertEqual(type(b_obj1.created_at), datetime)
            self.assertNotEqual(b_obj1.created_at, b_obj2.created_at)
            self.assertNotEqual(b_obj.created_at, b_obj.updated_at)

        def test_updated_at(self):
            """Tests the updated_at attribute"""
            self.assertTrue(hasattr(b_obj1, 'updated_at'))
            self.assertEqual(type(b_obj1.updated_at), datetime)
            self.assertNotEqual(b_obj1.updated_at, b_obj2.updated_at)


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
        self.assertEqual(obj_dict['created_at'], b_obj1.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], b_obj1.updated_at.isoformat())
        obj = BaseModel(**obj_dict)
        self.assertEqual(obj.to_dict(), b_obj1.to_dict())
        self.assertEqual(obj.to_dict(), obj_dict)
