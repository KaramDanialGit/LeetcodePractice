# TLE but it works!

from typing import List

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    result = 0
    m = len(matrix)
    n = len(matrix[0])

    def dfs(row, col, seen, tmpPath):
        nonlocal result
        seen[row][col] = 1
        tmpPath.append(matrix[row][col])
        result = max(result, len(tmpPath))

        if row - 1 >= 0 and not seen[row - 1][col] and matrix[row - 1][col] > tmpPath[-1]:
            dfs(row - 1, col, seen, tmpPath)
            tmpPath.pop()
        if row + 1 < m and not seen[row + 1][col] and matrix[row + 1][col] > tmpPath[-1]:
            dfs(row + 1, col, seen, tmpPath)
            tmpPath.pop()
        if col - 1 >= 0 and not seen[row][col - 1] and matrix[row][col - 1] > tmpPath[-1]:
            dfs(row, col - 1, seen, tmpPath)
            tmpPath.pop()
        if col + 1 < n and not seen[row][col + 1] and matrix[row][col + 1] > tmpPath[-1]:
            dfs(row, col + 1, seen, tmpPath)
            tmpPath.pop()
        seen[row][col] = 0
        return result

    for i in range(m):
        for j in range(n):
            seen = [[0] * n for _ in range(m)]
            dfs(i, j, seen, [])

    return result

test = [[7,8,9],[9,7,6],[7,2,3]]
print(longestIncreasingPath(test))