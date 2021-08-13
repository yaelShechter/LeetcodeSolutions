"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.
"""

def set_zeros_matrix(matrix: List[List[int]]) -> None:
    first_col = 0
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        if matrix[i][0] == 0:
            first_col = 1
            
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in reversed(range(1, m)):
        for j in reversed(range(1, n)):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        matrix[0] = [0] * n
    if first_col:
        for i in range(m):
            matrix[i][0] = 0
