#!/usr/bin/python3
"""
A module that contains a function that creates an Object
from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    :param filename: the name of the JSON file
    :return: None
    """
    with open(filename, encoding="UTF8") as f:
        json.load(f)
