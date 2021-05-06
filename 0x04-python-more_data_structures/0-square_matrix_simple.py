#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    def square(n):
        return n ** 2

    newMatrix = []

    for row in matrix:
        newMatrix.append([square(x) for x in row])

    return newMatrix
