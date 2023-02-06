#!/usr/bin/python3
"""
Define a child class that inherits from a Parent class
"""

class MyList(list):
    """Return a list of integers in sorted fashion
   
   Args:
        list(int): data structure containing elements to return in sorted form
    """

    def __init__(self):
        """initialize MyList object"""
        super().__init__()

    def print_sorted(self):
        """Return list in sorted form"""
        print(sorted(self))
