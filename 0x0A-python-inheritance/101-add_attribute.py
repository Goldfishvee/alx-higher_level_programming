#!/usr/bin/python3
"""Define a function that adds attributes to an object"""


def add_attribute(obj, attr, value):
    """Add an attribute to an object if possible
    
    Args:
        obj(any): object to add attribute to
        attr(str): name of attribute
        value(any): value of attribute
    Return:
        TypeError if attibute cannot be added
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
