#!/usr/bin/python3
"""
This module contains the FileStorage class.
"""


import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that serializes instances to a JSON file
        and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        Returns:
            The dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the object in __objects with the key <obj class name>.id.
        Args:
            obj: The object to be set in __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists).
        If the file doesn't exist, no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                object = json.load(file)
                for key, value in object.items():
                    FileStorage.__objects[key] =\
                        eval(value['__class__'])(**value)
        except FileNotFoundError:
            return
