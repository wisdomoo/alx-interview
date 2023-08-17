#!/usr/bin/python3
"""2D Rotation  Matrix Module
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    # get the length of the matrix
    n = len(matrix)

    # transpose the matrix to swap rows and columns
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row to rotate the matrix clockwise
    for i in range(n):
        matrix[i] = matrix[i][::-1]
