#!/usr/bin/python3
"""
This module provides a function to add
a new attribute to an object dynamically.
"""


def add_attribute(obj, attr1, attr2):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attr1 (str): The name of the attribute to add.
        attr2: The value of the attribute to add.

    Raises:
        TypeError: If the object does not support adding new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr1, attr2)
    else:
        raise TypeError("can't add new attribute")
