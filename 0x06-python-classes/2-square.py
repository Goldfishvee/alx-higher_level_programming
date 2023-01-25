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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = 
