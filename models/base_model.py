#!/usr/bin/python3

"""This is the base model
defines the base attr of the model
and it behaviour
"""
import uuid
import datetime
from datetime import datetime, timezone


class BaseModel:
    """Defines the base class"""
    def __init__(self):
        """Initilizes the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def __str__(self):
        """The string method"""
        return "[{}] ".format(type(self).__name__) +\
            "({}) ".format(self.id) +\
            "{}".format(self.__dict__)

    def save(self):
        """updates the public method 'updated_at'
        with the current datetime"""

        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        """Returns a dictionary representation containing
        all keys/values of __dict__ of the instance"""
        dict_vals = (self.__dict__).copy()
        dict_vals["created_at"] =\
            dict_vals["created_at"].isoformat()
        dict_vals["updated_at"] =\
            dict_vals["updated_at"].isoformat()
        dict_vals['__class__'] = type(self).__name__
        return dict_vals
