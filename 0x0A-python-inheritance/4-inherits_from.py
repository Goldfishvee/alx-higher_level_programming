#!/usr/bin/python3
"""
Define function that checks inheritance of class object
"""


def inherits_from(obj, a_class):
    """Check inheritance of object
    Arg:
        obj (any obj): target object whose inheritance is to be checked.
        a_class (type): class to match obj to.
    Return:
        True if is inherited from instance of a_class
        False if otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
