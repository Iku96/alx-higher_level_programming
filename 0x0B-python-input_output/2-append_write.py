#!/usr/bin/python3
"""
A module containing a function that appends
a string at the end of a text file (UTF8),
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    :param filename: the name of the file
    :param text: the string to be appended
    :return: number of added characters
    """
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
