#!/usr/bin/python3
"""
This module defines classes for geometric operations. It includes a base class
(BaseGeometry) with methods for area calculation and integer validation,
and a Rectangle class that inherits from BaseGeometry.
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
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inherited from BaseGeometry. This class
    validates the width and height using the integer_validator method from
    the BaseGeometry class and provides an implementation for area calculation.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is not greater than 0.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: The area of the rectangle, calculated as width * height.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string in the format '[Rectangle] width/height'.
        """
        return f'[Rectangle] {self.__width}/{self.__height}'
