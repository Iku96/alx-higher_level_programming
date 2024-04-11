#!/usr/bin/python3
# 3-say_my_name.py
# Ikundwila Mwambona <ikumwana@gmail.com>
"""
    This is the 3-say_my_name module
    It contains a function that prints: My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints a person's name.
    :param first_name:
    :param last_name:
    :return: None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Only add space if last_name is not an empty string.
    space = " " if last_name else ""
    print("My name is {}{}{}".format(first_name, space, last_name))
