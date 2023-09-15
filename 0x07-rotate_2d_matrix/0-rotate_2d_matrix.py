#!/usr/bin/python3
"""2D Matrix Array
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d square matrix 90 degrees clockwise in-place
    Args:
        matrix (list): 2d square matrix
    Return:
        None
    """
    n = len(matrix)

    # Step 1: Transpose the Matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse the Rows
    for i in range(n):
        matrix[i].reverse()
