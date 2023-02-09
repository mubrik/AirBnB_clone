#!/usr/bin/python3
""" Test Engine  """
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestEngine(unittest.TestCase):
    """ Base engine test cases """

    def setUp(self):
        """ setup """
        self.storage = storage
        self.storage.fpa = "test_db.json"
        self.instance = BaseModel()
        self.instance.name = "new"
        self.instance.number = 99
        self.instance.save()
        self.storage.reload()

    def tearDown(self):
        """ teardown """
        # delete old test file if created
        if (os.path.isfile(self.storage.fpa)):
            os.remove(self.storage.fpa)
        del self.storage

    def test_valid_new(self):
        """test new basemodel instance"""
        self.assertEqual(self.instance.name, "new")
        self.assertEqual(self.instance.number, 99)

    def test_valid_storage(self):
        """test new storage instance"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_empty(self):
        """test all storage method"""
        # remove created instance
        obj_data = self.instance.to_dict()
        attr_name = f"{obj_data['__class__']}.{obj_data['id']}"
        del storage.all()[attr_name]
        storage.save()
        self.assertEqual(self.storage.all(), {})

    def test_all_not_empty(self):
        """test all storage method"""
        self.storage.new(self.instance)
        obj_data = self.instance.to_dict()
        attr_name = f"{obj_data['__class__']}.{obj_data['id']}"
        self.assertEqual(self.storage.all()[f'{attr_name}'], self.instance)

    def test_new_valid(self):
        """test storage method new"""
        self.storage.new(self.instance)
        obj_data = self.instance.to_dict()
        attr_name = f"{obj_data['__class__']}.{obj_data['id']}"
        self.assertEqual(self.storage.all()[f'{attr_name}'], self.instance)

    def test_new_invalid(self):
        """test storage method new"""
        class Bad:
            pass
        bad_ins = Bad()
        with self.assertRaises(TypeError) as cm:
            self.storage.new(bad_ins)
        self.assertEqual(
            cm.exception.args[0], "Argument isnt a subclass of BaseModel")

    def test_new_empty(self):
        """test storage method new"""
        with self.assertRaises(ValueError) as cm:
            self.storage.new({})
        self.assertEqual(
            cm.exception.args[0], "Bad instance argument")

    def test_new_bad_value(self):
        """test storage method new"""
        with self.assertRaises(TypeError) as cm:
            self.storage.new("a bad string")
        self.assertEqual(
            cm.exception.args[0], "Argument isnt a subclass of BaseModel")
