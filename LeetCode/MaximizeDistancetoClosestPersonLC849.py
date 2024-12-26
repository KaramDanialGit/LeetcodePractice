from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        left, right = [N] * N, [N] * N
        result = 0

        for i in range(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        for i in range(N - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N - 1:
                right[i] = right[i + 1] + 1

        for i in range(N):
            if (seats[i] == 0):
                result = max(result, min(left[i], right[i]));
        print(left, right)
        return result