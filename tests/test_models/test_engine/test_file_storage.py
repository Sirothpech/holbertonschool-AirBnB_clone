#!/usr/bin/python3
"""
Unittests for the FileStorage class
"""
import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class
    """

    def setUp(self):
        """Set up test fixtures"""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_file_path_attribute(self):
        """Test the file_path attribute"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_attribute(self):
        """Test the objects attribute"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_method(self):
        """Test the all() method"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, self.storage._FileStorage__objects)

    def test_new_method(self):
        """Test the new() method"""
        user = User()
        user.id = "12345"
        self.storage.new(user)
        self.assertIn("User.12345", self.storage._FileStorage__objects)

    def test_save_method(self):
        """Test the save() method"""
        user = User()
        user.id = "12345"
        self.storage.new(user)
        self.storage.save()

        file_path = FileStorage._FileStorage__file_path
        self.assertTrue(os.path.isfile(file_path))

        with open(file_path, 'r') as file:
            data = json.load(file)
            self.assertIn("User.12345", data)

    def test_reload_method(self):
        """Test the reload() method"""
        user = User()
        user.id = "12345"
        self.storage.new(user)
        self.storage.save()

        self.storage.reload()

        all_objects = self.storage.all()
        self.assertIn("User.12345", all_objects)

    def test_reload_with_datetime_attribute(self):
        """Test the reload() method with datetime attribute"""
        current_time = datetime.now()
        base_model = BaseModel()
        base_model.id = "12345"
        base_model.created_at = current_time
        self.storage.new(base_model)
        self.storage.save()

        self.storage.reload()

        all_objects = self.storage.all()
        self.assertIn("BaseModel.12345", all_objects)
        self.assertIsInstance(all_objects["BaseModel.12345"].created_at,
                              datetime)
        self.assertEqual(all_objects["BaseModel.12345"].created_at,
                         current_time)


if __name__ == '__main__':
    unittest.main()
