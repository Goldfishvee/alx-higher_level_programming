#!/usr/bin/python3
"""Define new class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines child class of BaseGeometry"""
    def __init__(self, width, height):
        """initialize Rectangle
        
        Args:
            width(int): area width parameter of Rectangle
            height(int): area height parameter of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """implement and returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of object in Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
