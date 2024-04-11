#!/usr/bin/python3
# 4-print_square
# Ikundwila Mwambona <ikumwana@gmail.com>
"""
This is the 4-print_square module
It contains a function that prints a square with the character #
"""


def print_square(size):
    """This function prints a square with the character #

    Args:
        size: The size of the square.
    Returns:
        None.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for number in range(size):
        print("#" * size)
