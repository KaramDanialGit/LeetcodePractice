'''
Given a matrix of 1's and 0's, where 1's indicate an obstacle and 0's
indicate an available space to move. Reach the bottom right of the maze
starting from the top left and return the moves made to complete the path

start here ->	x x x x 0 0 0
			    0 0 0 x 0 0 0
			    0 0 1 x 1 1 1
			    0 0 1 x 1 1 1
			    1 1 1 x 1 1 1
			    0 0 0 x x x x 	<- finish here

moves: [(0,0), (0,1), (0,2), (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (5,4), (5,5), (5,6)]
'''


def maze_game_solver(arr):
    stack = []
    rows = len(arr)
    cols = len(arr[0])
    seen = [[0] * cols for _ in range(rows)]
    dfs(arr, 0, 0, stack, seen)

    print(stack)


def dfs(arr, i, j, stack, seen):
    rows = len(arr)
    cols = len(arr[0])

    stack.append((i, j))
    seen[i][j] = 1

    if i == rows - 1 and j == cols - 1:
        return True

    if i + 1 < rows and not seen[i + 1][j] and arr[i + 1][j] == 0:
        if dfs(arr, i + 1, j, stack, seen):
            return True
        stack.pop()
    if i - 1 >= 0 and not seen[i - 1][j] and arr[i - 1][j] == 0:
        if dfs(arr, i - 1, j, stack, seen):
            return True
        stack.pop()
    if j + 1 < cols and not seen[i][j + 1] and arr[i][j + 1] == 0:
        if dfs(arr, i, j + 1, stack, seen):
            return True
        stack.pop()
    if j - 1 >= 0 and not seen[i][j - 1] and arr[i][j - 1] == 0:
        if dfs(arr, i, j - 1, stack, seen):
            return True
        stack.pop()
    seen[i][j] = 0
    return False


matrix = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 1, 1, 1],
          [0, 0, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0]]

maze_game_solver(matrix)
