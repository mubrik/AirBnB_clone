#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Includes the class FileStorage which
serializes instances to a JSON file and deserializes JSON file to instances.
"""

import json


class FileStorage:
    """Defines common attributes for serialization and deserialization"""

    __file_path = "db.json"
    __objects = {}

    def __del__(self):
        """delete helper, useful for testing"""
        self.__objects = {}

    @property
    def fpa(self):
        """for convenience and testing"""
        return self.__file_path

    @fpa.setter
    def fpa(self, value):
        """for convenience and testing"""
        if not value or not isinstance(value, str):
            return
        self.__file_path = value

    def all(self):
        """returns the cls.__objects"""
        return self.__objects

    def new(self, obj):
        """sets the obj in cls.__objects"""
        if not obj:
            raise ValueError("Bad instance argument")
        if not self.validate_instance(obj):
            raise TypeError("Argument isnt a subclass of BaseModel")
        # safe instance
        obj_data = obj.to_dict()
        attr_name = f"{obj_data['__class__']}.{obj_data['id']}"
        self.__objects[attr_name] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        # checks
        if not self.__objects:
            return
        # validate all instances?
        new_objects = {
            k: v.to_dict() for (k, v) in self.__objects.items()}
        # open file, truncate if exist
        with open(self.__file_path, mode="w") as f:
            f.write(self.to_json_string(new_objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        # checks
        if not self.__file_path:
            return
        from models.base_model import BaseModel
        # read file
        try:
            with open(self.__file_path, mode="r") as f:
                json_str = f.read()
                obj = self.from_json_string(json_str)
                if not isinstance(obj, object):
                    raise TypeError("File JSON must be an object")
                # create a wrapper function to handle multiple class later
                self.__objects = {k: BaseModel(**v) for (k, v) in obj.items()}
        except FileNotFoundError as e:
            # raise or return hmm?
            pass

    def validate_instance(self, ins):
        from models.base_model import BaseModel
        return issubclass(type(ins), BaseModel)

    @staticmethod
    def to_json_string(dict_obj):
        """json string representation"""
        if not dict_obj:
            return "{}"
        if not isinstance(dict_obj, object):
            raise TypeError("Argument must be a dictionary")
        return json.dumps(dict_obj)

    @staticmethod
    def from_json_string(json_string):
        """deserialize json string"""
        if not json_string:
            raise TypeError("Valid string only")
        # using a try to keep method safe, remove later
        try:
            res = json.loads(json_string)
            return res
        except Exception as e:
            # re raising so i can test easily later
            raise TypeError("Bad JSON string")
