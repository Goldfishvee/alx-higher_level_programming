#!/usr/bin/python3
"""
Define a function that returns attributes and methods of an object
"""


def lookup(obj):
    """Returns the available attributes and methods of an object"""
    return (list(dir(obj)))
