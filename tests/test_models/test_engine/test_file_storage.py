#!/usr/bin/python3
"""
This module provides testing for the FileStorage class.
"""

import unittest
import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test fixture.
        """
        self.file_storage = FileStorage()

    def tearDown(self):
        """
        Clean up the test fixture.
        """
        self.file_storage = None

    def test_all_returns_dictionary(self):
        """
        Test that the all() method returns a dictionary.
        """
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_adds_object_to_all(self):
        """
        Test that the new() method adds an object to the all() dictionary.
        """
        user = User()
        self.file_storage.new(user)
        all_objects = self.file_storage.all()
        self.assertIn(f"User.{user.id}", all_objects)
        self.assertEqual(all_objects[f"User.{user.id}"], user)

    def test_save_writes_to_file(self):
        """
        Test that the save() method writes to the file.
        """
        user = User()
        self.file_storage.new(user)
        self.file_storage.save()

    def test_reload_loads_objects_from_file(self):
        """
        Test that the reload() method loads objects from the file.
        """
        self.file_storage.reload()
        self.file_storage.all()


if __name__ == "__main__":
    unittest.main()
