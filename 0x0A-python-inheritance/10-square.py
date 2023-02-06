#!/usr/bin/python3
"""Define child class that inherits from another child class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define a Square"""
    def __init__(self, size):
        """initialize Square
        
        Args:
            size(int): dimension of Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of Square"""
        return self.__size * self.__size
