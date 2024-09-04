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
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """Returns a string representation of the square

        Returns:
            str: A string in the format '[Square] id x/y - size'.
        """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - " \
               f"{self.__size}"
