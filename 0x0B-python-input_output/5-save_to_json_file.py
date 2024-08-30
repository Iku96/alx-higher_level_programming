#!/usr/bin/python3
"""
This module contains a function that writes
an Object to a text file using JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    :param my_obj: the object to be written to a text file
    :param filename: name of the file
    :return: None
    """
    with open(filename, "w", encoding="UTF8") as f:
        json.dump(my_obj, f)
