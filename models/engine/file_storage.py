#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Includes the class FileStorage which
serializes instances to a JSON file and deserializes JSON file to instances.
"""

from uuid import uuid4
from datetime import datetime
import json


class FileStorage:
    """Defines common attributes for serialization and deserialization """

    __file_path = "db.json"
    __objects = {}

    def all(self):
        """ returns the cls.__objects """
        return self.__objects

    def new(self, obj):
        """ sets the obj in cls.__objects"""
        # add validation later
        attr_name = f"{obj['__class__']}.{obj['id']}"
        self.__objects[attr_name] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        # checks
        if not self.__objects:
            return
        # open file, truncate if exist
        with open(self.__file_path, mode="w") as f:
            f.write(self.to_json_string(self.__objects))

    def reload(self):
        """ deserializes the JSON file to __objects """
        # checks
        if not self.__file_path:
            return
        # read file
        try:
            with open(self.__file_path, mode="r") as f:
                json_str = f.read()
                obj = self.from_json_string(json_str)
                if not isinstance(obj, object):
                    raise TypeError("File JSON must be an object")
                self.__objects = obj
        except FileNotFoundError as e:
            # raise or return hmm?
            pass

    @staticmethod
    def to_json_string(dict_obj):
        """ json string representation """
        if not dict_obj:
            return "{}"
        if not isinstance(dict_obj, object):
            raise TypeError("Argument must be a dictionary")
        return json.dumps(dict_obj)

    @staticmethod
    def from_json_string(json_string):
        """ deserialize json string """
        if not json_string:
            raise TypeError("Valid string only")
        # using a try to keep method safe, remove later
        try:
            res = json.loads(json_string)
            return res
        except Exception as e:
            # re raising so i can test easily later
            raise TypeError("Bad JSON string")
