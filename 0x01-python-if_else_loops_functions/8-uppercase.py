#!/usr/bin/python3
# 8-uppercase.py
# Author: Iku
"""
Function name: uppercase()
Description: Prints a string in uppercase followed by a new line
Prototype: def uppercase(str):
"""


def uppercase(str):
    """ Prints a string in uppercase followed by a new line """
    # Check is the string is empty
    if str == "":
        print()
    else:
        for char in str:
            # Convert string to ASCII code
            asciiCode = ord(char)
            if asciiCode >= 97 and asciiCode <= 122:
                asciiCode = asciiCode - 32
            # Convert ASCII back to characters
            char = chr(asciiCode)
            print("{}".format(char), end="")
    print()
