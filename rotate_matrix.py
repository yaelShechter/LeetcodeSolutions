def rotate_matrix(matrix: List[List[int]]) -> None:
    n = len(matrix) - 1
    max_cell = math.ceil(n / 2)
    for i in range(max_cell):
        for j in range(i, n - i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j][i]
            matrix[n - j][i] = matrix[n - i][n - j]
            matrix[n - i][n - j] = matrix[j][n - i]
            matrix[j][n - i] = tmp
            
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix(mat)
print(m)

#[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
