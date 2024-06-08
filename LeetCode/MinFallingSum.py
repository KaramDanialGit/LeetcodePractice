def minFallingPathSum(grid: list[list[int]]) -> int:
    n = len(grid)
    memo = {}

    def dfs(row, col):
        if row == n - 1:
            return grid[row][col]

        if (row, col) in memo:
            return memo[(row, col)]

        next_row_val = float('inf')
        for j in range(n):
            if j != col:
                next_row_val = min(next_row_val, dfs(row + 1, j))

        memo[(row, col)] = grid[row][col] + next_row_val
        return memo[(row, col)]

    result = float('inf')

    for i in range(n):
        result = min(result, dfs(0, i))

    return result


testCase = [[-37, 51, -36, 34, -22], [82, 4, 30, 14, 38], [-68, -52, -92, 65, -85], [-49, -3, -77, 8, -19],
            [-60, -71, -21, -62, -73]]
print(minFallingPathSum(testCase))
