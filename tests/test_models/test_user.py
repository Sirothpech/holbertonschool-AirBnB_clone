#!/usr/bin/python3
"""
Unittests for the User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test fixtures"""
        self.user = User()

    def test_user_attributes(self):
        """Test that user attributes are initialized correctly"""
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_user_save_method(self):
        """Test the save() method of User"""
        # Modify user attributes
        self.user.email = 'john@example.com'
        self.user.password = 'password'
        self.user.first_name = 'John'
        self.user.last_name = 'Doe'

        # Call the save() method
        self.user.save()

        # Verify if the modifications have been saved to the JSON file
        # Your code to check the content of the JSON file and validate
        # the user attributes

    def test_user_str_method(self):
        """Test the __str__() method of User"""
        self.user.email = 'john@example.com'
        self.user.password = 'password'
        self.user.first_name = 'John'
        self.user.last_name = 'Doe'

        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)


if __name__ == '__main__':
    unittest.main()
