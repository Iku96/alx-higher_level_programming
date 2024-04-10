#!/usr/bin/python3
# 2-matrix_divided.py
# Ikundwila Mwambona <ikumwana@gmail.com>

"""
This is the 2-matrix_divided module.
It contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix

    Args:
        matrix: The matrix who elements are to be divided.
        div: the number that the elements of the matrix are divided to.
    Returns:
        The dividend, which is the new matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if not matrix:
            raise ValueError("Matrix can't be empty")

        row_size = len(matrix[0])
        for row in matrix:
            if len(row) != row_size:
                raise TypeError("Each row of the matrix "
                                "must have the same size")

    new_matrix = [[round(element/div, 2) for element in row] for row in matrix]
    return new_matrix
