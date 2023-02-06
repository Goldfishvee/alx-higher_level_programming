#!/usr/bin/python3
"""
Check for object instance of class
"""


def is_same_class(obj, a_class):
    """check if object is an instance of a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
