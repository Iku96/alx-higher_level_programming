#!/usr/bin/python3
"""
Module contains a function that returns a list of integers
representing pascal's triangle of n
"""


def pascal_triangle(n):
    """
    :param n: no of rows of pascal's triangle
    :return: a list of integers representing
    pascal's triangle of n
    """
    triangle = []
    for rows in range(n):
        row = [1]
        if rows > 0:
            for col in range(1, rows):
                row.append(triangle[rows-1][col-1] + triangle[rows-1][col])
            row.append(1)
        triangle.append(row)

    return triangle
