#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        print()
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            print("{:d}".format(matrix[i][y]), end=' ')
        print("{}".format(""))
