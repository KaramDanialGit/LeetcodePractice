"""
Find leftmost smaller number in an array.
Suppose you are given an array [2, 1, 3, 2, 1, 3]
output should be [-1, -1, 2, 1, -1, 2]?

Constraints are each element of array must be in range 1 <= arr[i] <= m ?
Expected time complexity O(n + m).
"""

def leftMostSmaller(arr):
    n = len(arr)
    result = [-1] * n
    idxTracker = [10**9 for _ in range(n)]

    for index, value in enumerate(arr):
        idxTracker[value] = min(idxTracker[value], index)

    for value in arr:
        idxTracker[value] = min(idxTracker[value], idxTracker[value-1])

    for index in range(n):
        if idxTracker[arr[index] - 1] > index:
            continue
        else:
            result[index] = arr[idxTracker[arr[index] - 1]]
    print(result)

leftMostSmaller([2, 1, 3, 2, 1, 3])