def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    output = 0
    grid2Ones = []
    visited = set()

    for row in range(len(grid2)):
        for col in range(len(grid2[0])):
            if grid2[row][col] == 1:
                grid2Ones.append((row, col))

    def dfs(grid1, grid2, row, col, visited):
        nonlocal isValid

        if grid1[row][col] != 1 and grid2[row][col] == 1:
            isValid = False

        visited.add((row, col))

        if row - 1 >= 0 and grid2[row - 1][col] == 1 and (row - 1, col) not in visited:
            dfs(grid1, grid2, row - 1, col, visited)
        if row + 1 < len(grid2) and grid2[row + 1][col] == 1 and (row + 1, col) not in visited:
            dfs(grid1, grid2, row + 1, col, visited)
        if col - 1 >= 0 and grid2[row][col - 1] == 1 and (row, col - 1) not in visited:
            dfs(grid1, grid2, row, col - 1, visited)
        if col + 1 < len(grid2[0]) and grid2[row][col + 1] == 1 and (row, col + 1) not in visited:
            dfs(grid1, grid2, row, col + 1, visited)

    while grid2Ones:
        isValid = True
        current = grid2Ones.pop(0)

        if current not in visited:
            dfs(grid1, grid2, current[0], current[1], visited)
            if isValid:
                output += 1

    return output