# Given a set of n servers and their respective capacities at the ith index
# Determine the number of valid server configurations such that the first and last capacities are equal to the sum of
# intermediary capacities (ie. capacities[r + 1] capacities[l - 1]) with a minimum number of 3 capacities

# Example: [9,3,3,3,9]
# Valid server capacities: [3,3,3], [9,3,3,3,9]
# Invalid server capacities: [9,3,3], [3,3,9], [9,3,3,3], [3,3,3,9]
# Output: 2

def validServerConfiguration(capacities) -> int:
    result = 0
    n = len(capacities)

    if n < 3:
        return 0

    windowLen = 3

    for i in range(windowLen, n):
        for j in range(n):
            if i + j > n:
                break
            target = capacities[j]
            if target == sum(capacities[j+1:j+i-1]) and target == capacities[j+i-1]:
                result += 1

    target = capacities[0]
    if target == sum(capacities[1:n-1]) and target == capacities[-1]:
        result += 1

    return result

serverCaps = [9,3,3,3,9]
print(validServerConfiguration(serverCaps))