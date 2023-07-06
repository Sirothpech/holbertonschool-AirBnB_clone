#!/usr/bin/python3
"""
Unittests for the City class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for the City class."""

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test if City has the expected attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_attribute_types(self):
        """Test if City attributes have the correct types."""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == "__main__":
    unittest.main()
