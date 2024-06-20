import heapq
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N = len(bloomDay)
        minHeap = []
        latestDay = 0

        if m * k > N:
            return -1

        for day in bloomDay:
            heapq.heappush(minHeap, day)

        while m > 0:
            tmp = k
            print(m)

            while tmp > 0:
                latestDay = max(heapq.heappop(minHeap), latestDay)
                tmp -= 1

            m -= 1

        return latestDay