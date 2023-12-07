#!/usr/bin/python3
# 4-only_diff_elements.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set"""
    new_set = set_1 ^ set_2
    return new_set
