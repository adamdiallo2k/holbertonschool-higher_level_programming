#!/usr/bin/python3
"""module commented"""


def matrix_divided(matrix, div):
    """function commented"""
    err_msg = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(err_msg)

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(err_msg)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]

    return new_matrix
