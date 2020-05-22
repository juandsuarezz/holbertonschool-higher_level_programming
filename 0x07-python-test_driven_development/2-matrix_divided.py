#!/usr/bin/python3
"""Documentation of a function that divides the elements of a matrix"""


def matrix_divided(matrix, div):
    """Function that divides the elements of a matrix by an int or float
    
    Arguments:
        matrix (list): matrix to divide
        div (int or float): number to divide the matrix
    Returns:
        new matrix containing the divided numbers
    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
floats")
    if type(matrix) == tuple or type(matrix) == set:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if type(i) == tuple or type(i) == set:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")
    length = len(matrix[0])
    for matrices in matrix:
        if len(matrices) != length:
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")

    div_matrix = []
    for i in matrix:
        div_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return div_matrix
