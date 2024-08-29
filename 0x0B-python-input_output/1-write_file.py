#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file,
in UTF8 format, and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """

    :param filename: the name of the file
    :param text: the string to be written in the file
    :return:
        number of characters written
    """
    with open(filename, "w+", encoding="UTF8") as f:
        return f.write(text)


# Example usage
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
