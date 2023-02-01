#!/usr/bin/python3
"""
This is the "3-say_my_name" module

This module takes two arguments, say_ny_name(first_name, last_name).
It then returns a string made of first and last name
"""


def say_my_name(first_name, last_name=""):
    """print first and last name from an input"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
