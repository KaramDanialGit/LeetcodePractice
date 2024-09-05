"""
Given a matrix of an image containing only 1's and 0's, where 1 is black and 0 is white, convert all black pixels in the image not
connected to the border to white.

Input:
image = [
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0]
]

Output:
result = [
    [1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]
"""

def fixImage(image):
    rows = len(image)
    cols = len(image[0])
    safeOnes = set()

    def dfs(value, row, col):
        nonlocal safeOnes, rows, cols

        if value == 1:
            safeOnes.add((row, col))

        if row - 1 >= 0 and (row - 1, col) not in safeOnes and image[row - 1][col] == 1:
            dfs(image[row - 1][col], row - 1, col)
        if row + 1 < rows and (row + 1, col) not in safeOnes and image[row + 1][col] == 1:
            dfs(image[row + 1][col], row + 1, col)
        if col - 1 >= 0 and (row, col - 1) not in safeOnes and image[row][col - 1] == 1:
            dfs(image[row][col - 1], row, col - 1)
        if col + 1 < cols and (row, col + 1) not in safeOnes and image[row][col + 1] == 1:
            dfs(image[row][col + 1], row, col + 1)

    for col in range(cols):
        if image[0][col] == 1:
            dfs(image[0][col], 0, col)
        if image[rows - 1][col] == 1:
            dfs(image[rows - 1][col], rows - 1, col)

    for row in range(rows):
        if image[row][0] == 1:
            dfs(image[row][0], row, 0)
        if image[row][cols - 1] == 1:
            dfs(image[row][cols - 1], row, cols - 1)

    for row in range(rows):
        for col in range(cols):
            if image[row][col] == 1 and (row, col) not in safeOnes:
                image[row][col] = 0

    return image

test = [
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0]
]

result = fixImage(test)
for row in result:
    print(row)