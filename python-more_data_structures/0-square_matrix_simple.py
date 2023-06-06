#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_matrix = [[element ** 2 for element in row] for row in matrix]

    return new_matrix
