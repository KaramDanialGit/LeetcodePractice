# TLE but it's my TLE <3
from typing import Optional, List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def nodesBetweenCriticalPoints(head: Optional[ListNode]) -> List[int]:
    result = []
    minDist = float("inf")
    maxDist = float("-inf")

    prev = head
    current = prev.next
    next = current.next
    index = 1

    while next:
        if current.val > next.val and current.val > prev.val:
            result.append([current.val, index])
        if current.val < next.val and current.val < prev.val:
            result.append([current.val, index])
        prev = current
        current = next
        next = next.next
        index += 1

    N = len(result)
    if N < 2:
        return [-1, -1]

    for i in range(N):
        for j in range(i, N):
            if i != j:
                if result[j][1] - result[i][1] < minDist:
                    minDist = result[j][1] - result[i][1]
                if result[j][1] - result[i][1] > maxDist:
                    maxDist = result[j][1] - result[i][1]

    return [minDist, maxDist]

