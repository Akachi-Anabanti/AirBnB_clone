#!/usr/bin/python3
"""This is a test file for the base model"""
import unittest
from models.base_model import BaseModel
import datetime


class BaseModelTest(unittest.TestCase):

    def setUp(self):
        self.mod1 = BaseModel()
        self.mod1.my_number = 10
        self.mod1.my_name = "test base model"
        self.mod1_json = self.mod1.to_dict()

    def test_base_model_has_string_id(self):
        self.assertIsInstance(self.mod1.id, str)

    def test_base_model_has_date(self):
        self.assertTrue(type(self.mod1.created_at) == datetime.datetime)
        self.assertTrue(type(self.mod1.updated_at) == datetime.datetime)

    def test_base_model_updates_time(self):
        prev_update_at = self.mod1.updated_at
        self.mod1.save()
        new_update_at = self.mod1.updated_at
        self.assertTrue(new_update_at > prev_update_at)

    def test_base_model_converts_to_dict(self):
        self.assertIsInstance(self.mod1_json, dict)

    def test_base_model_dict_has_class_key(self):
        self.assertIn("__class__", self.mod1_json.keys())

    def test_base_model_has_instance_attribute_name_number(self):
        self.assertIn("my_number", self.mod1_json.keys())
        self.assertIn("my_name", self.mod1_json.keys())
