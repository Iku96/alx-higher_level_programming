#!/usr/bin/python3
"""Rectangle class
inherits from Base class
"""


class Base:
    """The base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height >= 0:
            self.__height = height
        else:
            raise ValueError("Height cannot be negative")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width >= 0:
            self.__width = width
        else:
            raise ValueError("Width cannot be negative")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x >= 0:
            self.__x = x
        else:
            raise ValueError(f"{self.__x} cannot be negative")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if y >= 0:
            self.__y = y
        else:
            raise ValueError(f"{self.__y} cannot be negative")


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)