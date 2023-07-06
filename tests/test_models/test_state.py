#!/usr/bin/python3
"""
Unittests for the State class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for the State class."""

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test if State has the expected attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_attribute_types(self):
        """Test if State attributes have the correct types."""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)


if __name__ == "__main__":
    unittest.main()
