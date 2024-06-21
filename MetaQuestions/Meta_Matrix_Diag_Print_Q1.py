import collections
'''
Given the matrix

[[1, 2, 3, 4, 5],
 [6, 7, 8, 9, 1, 1],
 [6, 3, 2, 4, 5]]

print the array's diagonals such that we see:

1
2 6
3 7 6
4 8 3
5 9 2
1 4
1 5
'''

def print_diagonals(matrix):
    rows = len(matrix)
    my_map = collections.defaultdict(list)

    for i in range(rows):
        cols = len(matrix[i])
        for j in range(cols):
            my_map[i + j].append(matrix[i][j])
    for key in my_map:
        print(my_map[key])

array = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 1, 1],
         [6, 3, 2, 4, 5]]

print_diagonals(array)