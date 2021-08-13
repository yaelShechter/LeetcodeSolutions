"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.
"""

def setZeroes(matrix) -> None:
    first_row = 0
    first_col = 0
    m = len(matrix)
    n = len(matrix[0])
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row == 0:
                    first_row = 1
                if col == 0:
                    first_col = 1
                else:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
    for row in reversed(range(1, m)):
        for col in reversed(range(1, n)):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0
    if first_row:
        matrix[0] = [0] * n
    if first_col:
        for i in range(m):
            matrix[i][0] = 0
