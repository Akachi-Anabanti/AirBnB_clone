#!/usr/bin/python3
"""This is a test file for the base model"""
import unittest
from models.base_model import BaseModel
import datetime


class BaseModelTest(unittest.TestCase):
    """The Base Model test case"""
    def setUp(self):
        """setup function"""
        self.mod1 = BaseModel()
        self.mod1.my_number = 10
        self.mod1.my_name = "test base model"
        self.mod1_json = self.mod1.to_dict()

    def test_base_model_has_string_id(self):
        """tests if the id is a string"""
        self.assertIsInstance(self.mod1.id, str)

    def test_base_model_has_date(self):
        """tests if the created_at and updated_at are
        datetime objects"""
        self.assertTrue(type(self.mod1.created_at) == datetime.datetime)
        self.assertTrue(type(self.mod1.updated_at) == datetime.datetime)

    def test_base_model_updates_time(self):
        """tests if the time updates when
        save method is called"""
        prev_update_at = self.mod1.updated_at
        self.mod1.save()
        new_update_at = self.mod1.updated_at
        self.assertTrue(new_update_at > prev_update_at)

    def test_base_model_converts_to_dict(self):
        """tests if the base_model succesful creates
        a dictionary object"""
        self.assertIsInstance(self.mod1_json, dict)

    def test_base_model_dict_has_class_key(self):
        """tests if the dictionary representation of the base
        model has the '__class__' in it"""
        self.assertIn("__class__", self.mod1_json.keys())

    def test_base_model_has_instance_attribute_name_number(self):
        """tests if the dictionary object contains new instance variables"""
        self.assertIn("my_number", self.mod1_json.keys())
        self.assertIn("my_name", self.mod1_json.keys())

    def test_base_model_instance_created_from_dict(self):
        """tests new instance is created from dict"""
        mod2 = BaseModel(**self.mod1_json)
        self.assertEqual(self.mod1.id, mod2.id)
        self.assertEqual(self.mod1.created_at, mod2.created_at)
        self.assertIsNot(mod2, self.mod1)
        self.assertNotIn('__class__', vars(mod2).keys())
