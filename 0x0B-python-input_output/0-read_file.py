#!/usr/bin/python3
"""
This module provides a function that reads the contents of a text file
and prints them to stdout
"""


def read_file(filename=""):
    """
    Reads the contents of a file with UTF-8 encoding and prints them
    to the console
    :param
        filename (str): The name of the file to read.
        if no filename is provided, it defaults to an empty string.
    :return:
        No return.
    """
    with open(filename, encoding="UTF8") as f:
        fileContents = f.read()
        print(fileContents, end="")
