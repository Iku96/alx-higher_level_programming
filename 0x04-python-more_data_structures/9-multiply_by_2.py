#!/usr/bin/python3
# 9-multiply_by_2.py
# Ikundwila N Mwambona <ikumwana@gmail.com>


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    new_dict = a_dictionary.copy()
    for key in new_dict.keys():
        new_dict[key] = new_dict[key] * 2
    return new_dict
