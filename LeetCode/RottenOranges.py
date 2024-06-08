# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# ------

# 1. identify all rotten oranges
# 2. perform bfs about each rotten orange index and increment minutes by 1
# 3. rot adjecent cells labeled as 1
# 4. scan through array and return -1 if one or more orange remains
# 5. if all rot return minutes

def rotten_oranges(oranges):
    rotten = []
    rows = len(oranges)
    cols = len(oranges[0])
    iteration = 0
    minute = 0

    if not oranges:
        return -1

    for i in range(rows):
        for j in range(cols):
            if oranges[i][j] == 2:
                rotten.append([i, j, iteration])

    tmp = iteration

    while rotten:
        row, col, iter = rotten.pop(0)

        if tmp != iter:
            minute += 1
            tmp = iter

        if row + 1 < rows and oranges[row + 1][col] == 1:
            oranges[row + 1][col] = 2
            rotten.append([row + 1, col, iter + 1])
        if row - 1 >= 0 and oranges[row - 1][col] == 1:
            oranges[row - 1][col] = 2
            rotten.append([row - 1, col, iter + 1])
        if col + 1 < cols and oranges[row][col + 1] == 1:
            oranges[row][col + 1] = 2
            rotten.append([row, col + 1, iter + 1])
        if col - 1 >= 0 and oranges[row][col - 1] == 1:
            oranges[row][col - 1] = 2
            rotten.append([row, col - 1, iter + 1])

    for i in range(rows):
        for j in range(cols):
            if oranges[i][j] == 1:
                return -1

    return minute


assert (rotten_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]])) == 4
assert (rotten_oranges([[2, 1, 1], [0, 1, 1], [1, 0, 1]])) == -1
assert (rotten_oranges([[0, 2]])) == 0

