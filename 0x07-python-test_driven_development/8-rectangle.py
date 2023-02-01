#!/usr/bin/python3
"""
Create a class Rectangle that defines
attributes of the geometrical figure
"""


class Rectangle():
    """define a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize Rectangle
        Args:
            width(int): define the width dimension
            height(int): define height dimension
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: get the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width of Rectangle
        Args:
            value(int): contains dimensional value of Rectangle width
        Return:
            numerical value of width
            if width is not an integer, raise a TypeError
            if width less than zero, raise a ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: get the height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height of Rectangle
        Args:
            value(int): contains dimensional height value of Rectangle
        Return:
            numerical value of height
            if height is less than zero, raise ValueError
            if height is not integer, raise TypeError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                          for i in range(self.__height)])

    def __repr__(self):
        """canonical string representation of object in Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete an instance in Rectangle"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare two instances of Rectahngle
        Args:
            rect_1 (obj): one instance of Rectangle
            rect_2 (obj): another instance of Rectangle
        Return:
            biggest rectangle based on area or rect_1 if both have area value
            raise TypeError if both rect_1 and rect_2 are not instances of
            Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
