#!/usr/bin/python3
"""
Base class
"""
import json


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
            file.write(Base.to_json_string(obj_dict))
