#!/usr/bin/python3
"""
This module contains a class that defines a Student
by first name, last name, and age.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            filtered_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered_dict[key] = self.__dict__[key]
            return filtered_dict

        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
