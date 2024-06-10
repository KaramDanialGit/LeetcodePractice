# REFERENCE: https://leetcode.com/discuss/interview-question/842141/Databricks-OA

def almostTetris(n, m, figures):
    grid = [[0] * m for _ in range(n)]

    shapes = {
        1: [(0, 0)],
        2: [(0, 0), (0, 1), (0, 2)],
        3: [(0, 0), (0, 1), (1, 0), (1, 1)],
        4: [(0, 0), (1, 0), (1, 1), (2, 0)],
        5: [(0, 0), (0, 1), (-1, 1), (0, 2)],
    }

    def checkShapeFit(x, y, shapes_no, number):
        for (i, j) in shapes[shapes_no]:
            if (x + i) >= n or (y + j) >= m or (x + i) < 0 or (y + j) < 0 or grid[x + i][y + j] != 0:
                return False

        for i, j in shapes[shapes_no]:
            grid[x+i][y+j] = number

    def getAvailability():
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    if checkShapeFit(row, col, f, i + 1):
                        return

    for i, f in enumerate(figures):
        getAvailability()

    print(grid)
    return grid


n = 4
m = 4
figures = [4, 2, 1, 3]
almostTetris(n, m, figures)
