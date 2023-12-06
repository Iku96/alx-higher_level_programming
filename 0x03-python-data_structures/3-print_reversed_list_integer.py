#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Ikundwila Mwambona <ikumwana@gmail.com>

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    my_list.reverse()
    for number in my_list:
        print("{:d}".format(number))
