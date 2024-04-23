#!/usr/bin/python3
# 7-rectangle.py
# Ikundwila Mwambona <ikumwana@gmail.com>
"""
This module defines a Rectangle class.
The rectangle class represents a rectangle with a width
and height.
The 'Rectangle' class provides methods to calculate the area
and perimeter of a rectangle.
The 'Rectangle' class returns the string representation of
a rectangle using the "#" character.
The 'Rectangle' class also returns the string formal
string representation of an object that can be used to recreate
the object.
The 'Rectangle' class prints a string when an instance is deleted.
The class contains a counter variable 'number_of_instances'
that keeps track of the number of instances created and deleted.
The class allow you to choose a string representation of any type,
but is initialized to '#' by default.
"""


class Rectangle:
    """Defines a  rectangle

    Attributes:
        width: the width of the rectangle, defaults to 0
        height: the height of the rectangle, defauls to 0
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initiatlizes a Rectangle instance.

        Args:
            width(int): the width of the rectangle, defaults to 0
            height(int): the height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates and returns the area of a rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates and returns the perimenter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of a rectangle using
        the "#" character."""
        if self.__height == 0 or self.__width == 0:
            return ""
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Returns the string representation of the rectangle that
         can be used to recreate the object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a string when an instance of a
        rectangle class is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
