from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fish = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col, visited):
            nonlocal rows, cols

            if ((row, col) in visited or row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0):
                return 0

            path = grid[row][col]
            visited.add((row, col))

            path += dfs(row + 1, col, visited)
            path += dfs(row - 1, col, visited)
            path += dfs(row, col + 1, visited)
            path += dfs(row, col - 1, visited)

            return path

        for i in range(rows):
            for j in range(cols):
                visited = set()
                if grid[i][j] > 0:
                    temp_fish = dfs(i, j, visited)
                    if temp_fish > max_fish:
                        max_fish = temp_fish

        return max_fish