#!/usr/bin/python3
# 0-square_matrix_simple.py
# Ikundwila N Mwambona <ikumwana@gmail.com>


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix

        Args: matrix=[]
        Returns: new matrix
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)
    return new_matrix
