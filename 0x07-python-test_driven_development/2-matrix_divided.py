#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
This modules supplies two arguments, matrix_divided(matrix, div)
where each element in the matrix is divided by a vector.
"""


def matrix_divided(matrix, div):
    """divide all elements of a matrix"""
    if (not isinstance(matrix, list) or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(isinstance(element, int) or isinstance(element, float)
                   for element in [item for row in matrix for item in row])):
        raise TypeError("matrix must be a matrix (lists of lists)"
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
