"""
Return true if an array contains a number. Otherwise, return false
"""


def binary_search(array, target):
    mid = len(array) // 2
    value = array[mid]

    if len(array) == 1 and value != target:
        return False

    if value == target:
        return True
    if value > target:
        return binary_search(array[:mid], target)
    if value < target:
        return binary_search(array[mid:], target)

    return False


test = [1, 2, 3, 4, 5]
target = 3

print(binary_search(test, target))
