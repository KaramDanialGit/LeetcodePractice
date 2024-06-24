# Find the longest diagonal in a matrix following the pattern 1,2,0,2,0....

def solution(matrix):
    max_pattern_length = 1
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                pattern_length_1 = diagonal_search(matrix, i, j, "top-right", [1])
                pattern_length_2 = diagonal_search(matrix, i, j, "top-left", [1])
                pattern_length_3 = diagonal_search(matrix, i, j, "bottom-right", [1])
                pattern_length_4 = diagonal_search(matrix, i, j, "bottom-left", [1])
                max_pattern_length = max(pattern_length_1, pattern_length_2, pattern_length_3, pattern_length_4, max_pattern_length)

    return max_pattern_length


def diagonal_search(matrix, i, j, direction, pattern):
    pattern_length = 1
    rows = len(matrix)
    cols = len(matrix[0])

    if direction == "top-right":
        while 0 <= i < rows and j >= 0 and j < cols:
            i -= 1
            j += 1

            if i < 0 or j >= cols:
                break

            if pattern[-1] == 1:
                if matrix[i][j] == 2:
                    pattern_length += 1
                    pattern.append(matrix[i][j])
                else:
                    return pattern_length
            elif pattern[-1] == 0 and matrix[i][j] == 2:
                pattern_length += 1
                pattern.append(matrix[i][j])
            elif pattern[-1] == 2 and matrix[i][j] == 0:
                pattern_length += 1
                pattern.append(matrix[i][j])
    if direction == "top-left":
        while 0 <= i < rows and j >= 0 and j < cols:
            i -= 1
            j -= 1

            if i < 0 or j < 0:
                break

            if pattern[-1] == 1:
                if matrix[i][j] == 2:
                    pattern_length += 1
                    pattern.append(matrix[i][j])
                else:
                    return pattern_length
            elif pattern[-1] == 0 and matrix[i][j] == 2:
                pattern_length += 1
                pattern.append(matrix[i][j])
            elif pattern[-1] == 2 and matrix[i][j] == 0:
                pattern_length += 1
                pattern.append(matrix[i][j])
    if direction == "bottom-left":
        while 0 <= i < rows and j >= 0 and j < cols:
            i += 1
            j -= 1

            if j < 0 or i >= rows:
                break

            if pattern[-1] == 1:
                if matrix[i][j] == 2:
                    pattern_length += 1
                    pattern.append(matrix[i][j])
                else:
                    return pattern_length
            elif pattern[-1] == 0 and matrix[i][j] == 2:
                pattern_length += 1
                pattern.append(matrix[i][j])
            elif pattern[-1] == 2 and matrix[i][j] == 0:
                pattern_length += 1
                pattern.append(matrix[i][j])

    if direction == "bottom-right":
        while 0 <= i < rows and j >= 0 and j < cols:
            i += 1
            j += 1

            if j >= cols or i >= rows:
                break

            if pattern[-1] == 1:
                if matrix[i][j] == 2:
                    pattern_length += 1
                    pattern.append(matrix[i][j])
                else:
                    return pattern_length
            elif pattern[-1] == 0 and matrix[i][j] == 2:
                pattern_length += 1
                pattern.append(matrix[i][j])
            elif pattern[-1] == 2 and matrix[i][j] == 0:
                pattern_length += 1
                pattern.append(matrix[i][j])

    return pattern_length