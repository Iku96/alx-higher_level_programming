#!/usr/bin/python3

from models.rectangle import Rectangle
"""Inherits from the rectangle class
"""


class Square(Rectangle):
    """Represents a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - " \
               f"{self.__size}"
