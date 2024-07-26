# Given a grid of integer values, determine the maximum path sum starting from [0, 0] and ending in the bottom right corner.
from typing import List

def maxPathSolver(grid: List[List[int]]):
    total = 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(1, rows):
        grid[0][i] += grid[0][i - 1]

    for i in range(1, cols):
        grid[i][0] += grid[i - 1][0]

    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])

    return grid[rows - 1][cols - 1]


test = [
    [1, 3, 6, 1],
    [2, 5, 9, 6],
    [4, 8, 5, 3],
    [0, 50, 2, 1],
]

answer = maxPathSolver(test)
print(answer)