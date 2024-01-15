#!/usr/bin/python3
"""File storage engine"""
import json


file_path = "file.json"


class FileStorage:
    __file_path = file_path  # string - path to the JSON file
    __objects = {}  # dictionary - stores all objects by <class name>.id

    def all(self):
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class  name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        "deserializes the JSON file to __objects"
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        try:
            with open(self.__file_path, 'r') as f:

                self.__objects =\
                        {k: BaseModel(**v) if k.startswith("BaseModel") else
                            User(**v) if k.startswith("User") else
                            Place(**v) if k.startswith("Place") else
                            City(**v) if k.startswith("City") else
                            Amenity(**v) if k.startswith("Amenity") else
                            State(**v) if k.startswith("State") else
                            Review(**v) for k, v in json.load(f).items()
                         }
        except FileNotFoundError:
            pass

    def delete(self, instance_key):
        """Deletes object from storage"""
        del self.__objects[instance_key]
