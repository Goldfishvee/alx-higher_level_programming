#!/usr/bin/python3

"""

This is the "4-print_square" module.

It supplies only one argument, print_square(size),

which prints the dimension of a square represented by a #.

"""

def print_square(size):

    """print a square using #"""

    if not isinstance(size, int) and not isinstance(size, float):

        raise TypeError("size must be an integer")

    if size < 0:

        raise ValueError("size must be >= 0")

    if size > 0:

        print(("#" * size + "\n") * size, end="")
