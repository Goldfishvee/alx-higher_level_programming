#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """create an instance of the class Square"""

    def __init__(self, size=0):
        """Initiliaze and validate attribute of the class Square.
        Args:
        __size (int): private instance of the class Square.
        Determines the size of the class Square.
        """
        self.__size = size

    @property
    def size(self):
        """int: get the size of the class Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method returns square of current area"""
        return self.__size * self.__size
