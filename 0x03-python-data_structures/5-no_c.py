#!/usr/bin/python3
# 5-no_c.py
# Iku <ikumwana@gmail.com>


def no_c(my_string):
    """Removes all characters C and c from a string"""
    my_string = my_string.lower()
    charToRemove = 'c'
    newString = ''.join([c for c in my_string if c != charToRemove])
    return newString
