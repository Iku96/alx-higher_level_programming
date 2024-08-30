#!/usr/bin/python3
"""
This module contains a function that returns
the JSON representation of an object(string).
"""
import json


def to_json_string(my_obj):
    """
    param
        my_obj: the object to be parsed
    :return:
        a JSON repr of the object (string format)
    """
    return json.dumps(my_obj)
