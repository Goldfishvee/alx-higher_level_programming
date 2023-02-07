#!/usr/bin/python3
"""Define a child class that inherits inverse characteristics from Parent"""


class MyInt(int):
    """inverts operators == and !="""
    def __eq__(self, value):
        """invert == operator with != operator

        Args:
            value(int): object value to invert
        """
        return self.real != value

    def __ne__(self, value):
        """invert != operator with == operator

        Args:
            value(int): object value to invert
        """
        return self.real == value
