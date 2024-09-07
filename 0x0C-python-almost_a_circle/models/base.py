#!/usr/bin/python3
"""
Base class
"""
import json
import os


class Base:
    """The base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"

        with open(filename, "w", encoding="UTF8") as file:
            if list_objs is None:
                return file.write("[]")
            else:
                obj_dict = []
                for obj in list_objs:
                    obj_dict.append(obj.to_dictionary())
                # obj_dict = [obj.__dict__ for obj in list_objs]
            file.write(cls.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            json_dict = json.loads(json_string)
            return json_dict

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, "r", encoding="UTF8") as file:
                json_string = file.read()
                list_of_dicts = cls.from_json_string(json_string)
                new_dict = []
                for dictionary in list_of_dicts:
                    new_dict.append(cls.create(**dictionary))
                return new_dict
