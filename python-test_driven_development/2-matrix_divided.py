 #!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This function divides all elements of a given matrix by a given number div.
    
    Args:
    matrix (list of lists): The matrix to be divided. The matrix must be a list of lists of integers/floats.
    div (int or float): The number by which the matrix elements should be divided.
    
    Returns:
    list of lists: A new matrix with all elements rounded to 2 decimal places after being divided by div.
    
    Raises:
    TypeError: If matrix is not a list of lists of integers/floats or if div is not a number.
    TypeError: If the matrix rows are of different sizes.
    ZeroDivisionError: If div is zero.
    
    Example:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
    [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]

