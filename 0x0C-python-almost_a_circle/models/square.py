#!/usr/bin/python3
""""Square class that inherits from
the Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square class

    This class inherits from the rectangle class and
    represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square.
            Defaults to 0.
            id (int, optional): The unique identifier of the square.
            Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.__x = x
        self.__y = y

    def __str__(self):
        """Returns a string representation of the square

        Returns:
            str: A string in the format '[Square] id x/y - size'.
        """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - " \
               f"{self.width}"

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size
