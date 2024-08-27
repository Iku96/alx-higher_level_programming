#!/usr/bin/python3
"""
This module defines a function to retrieve the list of attributes and methods
available for a given object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing a single list of strings, each representing
        an attribute or method name available in the object.
    """
    result = [dir(obj)]
    return result
