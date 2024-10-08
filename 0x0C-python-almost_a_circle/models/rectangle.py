#!/usr/bin/python3
"""Rectangle class
inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle, that inherits from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle.
            Defaults to 0.
            id (int, optional): The unique identifier of the rectangle.
            Defaults to None.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width or height is less than or equal to 0,
            or if x or y is less than 0.
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter method for the width attribute of the
        Rectangle class.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle.

        Args:
            width (int): The width of the rectangle.
            It must be an integer and greater than 0.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is not greater than 0.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle.

        Args:
            height (int): The height of the rectangle.
            Must be an integer greater than 0.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equal to 0.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        Property to get the value of the private attribute __x.

        Returns:
            int: The value of __x.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the x-coordinate of the rectangle.

        Args:
            x (int): The new x-coordinate.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.

        Returns:
            None
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        Getter method for the y attribute of the
        Rectangle class.

        Returns:
            int: The value of the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets the value of the y attribute of the
        Rectangle instance.

        Args:
            y (int): The new value of y.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints out the rectangle using the # character.
        """
        for row in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        The string representation is in the format:
        [Rectangle](<id>) <x>/<y> - <width>/<height>

        Where:
        - <id> is the unique identifier of the rectangle.
        - <x> and <y> are the x and y coordinates of the rectangle.
        - <width> and <height> are the width and height of the rectangle.

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
               f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance.

        Args:
            *args: Variable length argument list.
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
