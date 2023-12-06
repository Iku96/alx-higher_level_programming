#!/usr/bin/python3
# 6-print_matrix_integer.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def print_matrix_integer(matrix=([])):
    """Prints a matrix of integers"""
    for row in matrix:
        print(" ".join("{:d}".format(num)for num in row))
