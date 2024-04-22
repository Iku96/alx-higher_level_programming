#!/usr/bin/python3
# 1-rectangle.py
# Ikundwila Mwambona <ikumwana@gmail.com>
"""
This module defines a Rectangle class.
The rectangle class represents a rectangle with a width
and height.
"""


class Rectangle:
    """Defines a  rectangle

    Attributes:
        width: the width of the rectangle, defaults to 0
        height: the height of the rectangle, defauls to 0
    """
    def __init__(self, width=0, height=0):
        """
        Initiatlizes a Rectangle instance.

        Args:
            width(int): the width of the rectangle, defaults to 0
            height(int): the height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of a rectangle.

        Args:
            value(int): the new width of the rectangle.

        Raises:
            TypeError if value is not an integer.
            ValueError if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value(int): the new height of the rectangle.

        Raises:
            TypeError if value is not an integer
            ValueError if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
