#!/usr/bin/python3
# 0-add_integer.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def add_integer(a, b=98):
    """This function adds two integers together.

    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    Returns:
        The sum of a and b (a + b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
