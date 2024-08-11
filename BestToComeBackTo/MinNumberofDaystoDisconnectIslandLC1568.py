from typing import List

def minDays(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    oneIdx = []
    visited = set()

    def dfs(row, col):
        if (row, col) in visited:
            return

        visited.add((row, col))

        if row + 1 < rows and grid[row + 1][col] == 1:
            dfs(row + 1, col)
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            dfs(row - 1, col)
        if col + 1 < cols and grid[row][col + 1] == 1:
            dfs(row, col + 1)
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            dfs(row, col - 1)

    numIslands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                oneIdx.append((i, j))
            if grid[i][j] == 1 and (i, j) not in visited:
                dfs(i, j)
                numIslands += 1

    if numIslands >= 2 or numIslands == 0:
        return 0

    while oneIdx:
        numIslands = 0
        row, col = oneIdx.pop(0)
        visited = set()


        grid[row][col] = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
                    numIslands += 1

        if numIslands >= 2 or numIslands == 0:
            return 1

        grid[row][col] = 1

    return 2
