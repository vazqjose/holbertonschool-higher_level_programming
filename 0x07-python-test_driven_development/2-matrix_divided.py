#!/usr/bin/python3
"""
Function that divides each element of a matrix and returns a new matrix

Args:
    matrix: Input matrix to divide
    div: Number to be divided by (cant be 0)

Returns:
    New matrix
"""


def matrix_divided(matrix, div):
    """ Divides each of the elements of matrix by div """

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = []
    rowlen = len(matrix[0])

    for row in matrix:

        myRow = []

        for col in row:

            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a \
                        matrix (list of lists) \
                        of integers/floats")

            if type(div) is int or type(div) is float:
                myRow.append(round(col / div, 2))
            else:
                raise TypeError("div must be a number")

        if len(myRow) == rowlen:
            newMatrix.append(myRow)
        else:
            raise TypeError("Each row of the matrix must have the same size")

    return newMatrix
