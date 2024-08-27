#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of
a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited (directly
    or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if `obj` is an instance of a subclass of `a_class`, but
        not an instance of `a_class` itself. False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
