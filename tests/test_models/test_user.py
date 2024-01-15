#!/usr/bin/python3
"""Test file for the user model"""
from models.user import User
import unittest


class UserModelTest(unittest.TestCase):
    """Defines the test cases for the user model"""

    def test_user_is_created(self):
        """Tests to see if user is sucessfully created"""
        import datetime

        new_user = User()
        self.assertIsInstance(new_user.created_at, datetime.datetime)

    def test_user_created_from_dict(self):
        """Tests user model created from dict"""
        from datetime import timedelta
        from datetime import datetime
        from uuid import uuid4

        created_at = datetime.now() - timedelta(days=3)
        updated_at = created_at + timedelta(days=1)
        user_dict = {
                "id": str(uuid4()),
                "email": "test@email.com",
                "password": "password@test",
                "first_name": "user_firstname",
                "last_name": "user_lastname",
                "created_at": created_at.isoformat(),
                "updated_at": updated_at.isoformat(),
                }
        new_user = User(**user_dict)
        self.assertIn("id", new_user.to_dict().keys())

    def test_two_user_models_not_equal(self):
        """Test inequality of two instance model"""
        new_user1 = User()
        new_user2 = User()
        self.assertIsNot(new_user1, new_user2)
