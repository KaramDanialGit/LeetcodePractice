# RESOURCE: https://leetcode.com/discuss/interview-question/1202083/Databricksor-Online-Assessment-or-FigureUnderGravity
import collections

def FigureUnderGravity(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    min_fall_height = float('inf')
    copy_matrix = [["."]*cols for _ in range(rows)]

    for i in range(cols):
        f_begin = False
        first_f = float('-inf')
        for j in range(rows):
            if matrix[j][i] == "F":
                first_f = j
                f_begin = True
            if matrix[j][i] == "#" and f_begin:
                min_fall_height = min(min_fall_height, j - first_f)
                copy_matrix[j][i] = "#"
                f_begin = False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "F" and i + min_fall_height < rows:
                copy_matrix[i + min_fall_height - 1][j] = "F"
    print(copy_matrix)

matrix = [
["F", "F", "F"],
[".", "F", "."],
[".", "F", "F"],
["#", "F", "."],
["F", "F", "."],
[".", ".", "."],
[".", ".", "#"],
[".", ".", "."]
]

FigureUnderGravity(matrix)