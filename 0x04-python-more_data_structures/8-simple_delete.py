#!/usr/bin/python3
# 8-simple_delete.py
# Ikundwila N Mwambona <ikumwana@gmail.com>


def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary"""
    if key not in a_dictionary:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
