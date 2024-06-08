grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
n = len(grid)
m = len(grid[0])


def changeRow(matrix, row):
    for col in range(m):
        if matrix[row][col] == 1:
            matrix[row][col] = 0
        elif matrix[row][col] == 0:
            matrix[row][col] = 1


def changeCol(matrix, col):
    for row in range(n):
        if matrix[row][col] == 1:
            matrix[row][col] = 0
        else:
            matrix[row][col] = 1


def moreOnesInCol(matrix, col):
    numOnes = 0
    for row in range(n):
        if matrix[row][col] == 1:
            numOnes += 1
    return numOnes > (n - numOnes)


def matrixScore(matrix: list[list[int]]) -> int:
    for row in range(n):
        if matrix[row][0] != 1:
            changeRow(matrix, row)

    for col in range(0, m):
        if not moreOnesInCol(matrix, col):
            changeCol(matrix, col)

    result = 0
    return result


matrixScore(grid)
