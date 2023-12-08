#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    for keys in sorted(a_dictionary):
        print("{}: {}".format(keys, a_dictionary[keys]))
