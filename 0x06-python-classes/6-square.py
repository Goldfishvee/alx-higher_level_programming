#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """create an instance of the class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiliaze and validate attribute of the class Square.
        Args:
        __size (int): private instance of the class Square.
        Determines the size of the class Square.
        __position (int, int): private instance of the class Square.
        Determines the coordinates of the class Square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """int, int: get the coordinates of the class Square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """method returns square of current area"""
        return self.__size * self.__size

    def my_print(self):
        """method prints square with # to stdout"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
