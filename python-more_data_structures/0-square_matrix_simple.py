#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_matrix = [matrix[i] ** 2 for i in range(len(matrix))]

    return new_matrix