#!/usr/bin/python3
"""
Unittests for the FileStorage class
"""

import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

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
        user.save()

        all_objects = self.storage.all()
        self.assertIn("User.12345", all_objects)

    def test_save_method(self):
        """Test the save() method"""
        user = User()
        user.id = "12345"
        user.save()

        file_path = FileStorage._FileStorage__file_path
        self.assertTrue(os.path.isfile(file_path))

        with open(file_path, 'r') as file:
            data = json.load(file)
            self.assertIn("User.12345", data)

    def test_reload_method(self):
        """Test the reload() method"""
        user = User()
        user.id = "12345"
        user.save()

        file_path = FileStorage._FileStorage__file_path

        # Modify the content of the JSON file
        with open(file_path, 'r+') as file:
            data = json.load(file)
            data["FakeObject"] = {"id": "54321"}
            file.seek(0)
            json.dump(data, file)
            file.truncate()

        self.storage.reload()

        all_objects = self.storage.all()
        self.assertIn("User.12345", all_objects)
        self.assertNotIn("FakeObject.54321", all_objects)

if __name__ == '__main__':
    unittest.main()
