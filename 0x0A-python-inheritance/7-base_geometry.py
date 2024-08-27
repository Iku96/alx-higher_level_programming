#!/usr/bin/python3
"""
This module defines a base class for geometric operations, called BaseGeometry.
It includes methods for area calculation and integer validation.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations. This class provides a method
    to calculate the area (which is not implemented) and a method to validate
    integer values.
    """

    def __init__(self):
        """
        Initializes an instance of the BaseGeometry class.
        """
        pass

    def area(self):
        """
        Raises an Exception to indicate that the area calculation method
        is not implemented.

        Raises:
            Exception: Always raised with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is not greater than 0.
        """
        if isinstance(value, int) is False:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
