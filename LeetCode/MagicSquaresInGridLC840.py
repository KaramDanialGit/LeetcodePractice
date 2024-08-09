from typing import List

def numMagicSquaresInside(grid: List[List[int]]) -> int:
    magicSquares = 0
    n = len(grid)
    m = len(grid[0])

    if n < 3 or m < 3:
        return 0

    def isMagical(row, col):
        rowSums = []
        colSums = []
        diag1 = []
        diag2 = []
        visited = set()

        for i in range(3):
            rowSums.append(0)
            colSums.append(0)

            for j in range(3):
                if grid[row + i][col + j] in visited:
                    return 0

                if i == j:
                    diag1.append(grid[row + i][col + j])
                if i == 0 and j == 2 or i == 2 and j == 0:
                    diag2.append(grid[row + i][col + j])

                rowSums[i] += grid[row + j][col + i]
                colSums[i] += grid[row + i][col + j]

                visited.add(grid[row + i][col + j])

                if grid[row + i][col + j] < 1 or grid[row + i][col + j] > 9:
                    return 0

        diag2.append(grid[row + 1][col + 1])
        diag1Sum = sum(diag1)
        diag2Sum = sum(diag2)

        print(rowSums, colSums, diag1Sum, diag2Sum)

        if diag1Sum == diag2Sum:
            for i in range(3):
                for j in range(3):
                    if rowSums[i] != colSums[j]:
                        return 0
            return 1

        return 0

    for i in range(n - 2):
        for j in range(m - 2):
            magicSquares += isMagical(i, j)

    return magicSquares