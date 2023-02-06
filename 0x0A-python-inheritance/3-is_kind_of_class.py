#!/usr/bin/python3
"""
Check object inheritance from a class
"""


def is_kind_of_class(obj, a_class):
    """Check object is an instance of a class or is inherited from a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
