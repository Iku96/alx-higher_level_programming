#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Ikundwila Mwambona <ikumwana@gmail.com>

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    for number in reversed(my_list):
        if isinstance(number, int):
            print("{:d}".format(number))
