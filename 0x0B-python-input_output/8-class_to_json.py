#!/usr/bin/python3
"""
This module contains a function that returns
the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""


def class_to_json(obj):
    """
    :param obj: an instance of a class
    :return: a dictionary
    """
    return obj.__dict__
