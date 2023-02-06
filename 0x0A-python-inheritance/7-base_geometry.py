#!/usr/bin/python3
"""Define class BaseGeometry"""


class BaseGeometry():
    """define BaseGeometry"""
    def area(self):
        """define area of geometry - currently not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate instance value of method
        
        Args:
            name(str): name of object
            value(int): value of object to be validated
        Return:
            TypeError if value is not integer
            Valueerror if value is less than zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
