#!/usr/bin/python3
# 7-update_dictionary.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary"""
    a_dictionary.update({key: value})
    return a_dictionary
