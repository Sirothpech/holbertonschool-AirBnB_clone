#!/usr/bin/python3
"""
Unittests for the Amenity class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for the Amenity class."""

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test if Amenity has the expected attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_attribute_types(self):
        """Test if Amenity attributes have the correct types."""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.name, str)


if __name__ == "__main__":
    unittest.main()
