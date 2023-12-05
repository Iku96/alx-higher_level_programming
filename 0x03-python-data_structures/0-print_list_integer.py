#!/usr/bin/python3
# 0-print_list_integer.py
# Ikundwila Mwambona <ikumwana@gmail.com>

def print_list_integer(my_list=[]):
    """Prints all integers of a list"""
    for number in my_list:
        print("{:d}".format(number))
