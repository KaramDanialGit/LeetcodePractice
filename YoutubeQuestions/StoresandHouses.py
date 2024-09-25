"""
You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional).
For each house, find the store closest to it.
Return an integer array result where result[i] should denote the location of the store closest to the i-th house. If many
stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there
may be multiple stores and houses at the same location.

Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation:
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.

Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
Output: [2, 3, 2]

Input: houses = [4, 8, 1, 1], stores = [5, 3, 1, 2, 6]
Output: [3, 6, 1, 1]
"""

def binarySearch(stores, house, left, right, distance, prevDist):
    if left >= right:
        return distance

    mid = left + (right - left) // 2

    if stores[mid] == house:
        distance = house
        return distance

    if abs(stores[mid] - house) < abs(distance - house):
        distance = stores[mid]

    if distance == prevDist:
        return distance

    if stores[mid] > house:
        return binarySearch(stores, house, left, mid, distance, prevDist)
    else:
        prevDist = distance
        return binarySearch(stores, house, mid + 1, right, distance, prevDist)

def determineDistances(houses, stores):
    result = []
    stores.sort()

    for house in houses:
        minDistance = binarySearch(stores, house, 0, len(stores), 10**5, house)
        result.append(minDistance)

    return result


houses = [2, 4, 2]
stores = [5, 1, 2, 3]

print(determineDistances(houses, stores))