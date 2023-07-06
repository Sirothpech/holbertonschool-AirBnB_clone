#!/usr/bin/python3
"""
Unittests for testing instantiation of the Base_model class.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the Base_model class."""
    def setUp(self):
        self.model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_save_method(self):
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_from_dict_method(self):
        model_dict = {
            '__class__': 'BaseModel',
            'id': '12345',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T12:00:00.000000'
        }
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, '12345')
        self.assertEqual(new_model.created_at.isoformat(), '2022-01-01T12:00:00')
        self.assertEqual(new_model.updated_at.isoformat(), '2022-01-01T12:00:00')

if __name__ == "__main__":
    unittest.main()
