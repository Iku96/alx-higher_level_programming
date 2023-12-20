#!/usr/bin/python3
# 1-safe_print_integer.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def safe_print_integer(value):
    """Prints an integer with "{:d}".format()"""
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except TypeError:
        print("The value you passed was not an integer.")
