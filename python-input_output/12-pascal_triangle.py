#!/usr/bin/python3
"""module that adds all arguments to a Python list, and then saved to a file"""


def pascal_triangle(n):
    """commented fun tio,"""
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle
