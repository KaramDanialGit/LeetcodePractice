from typing import List

class Solution:
    def __init__(self):
        self.memo = {}

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = [1, 7, 30]

        def dfs(index: int) -> int:
            if index >= len(days):
                return 0

            if index in self.memo:
                return self.memo[index]

            min_cost = float('inf')

            for i in range(3):
                ticket_duration = travel[i]
                cost = costs[i]

                next_index = index
                while next_index < len(days) and days[next_index] < days[index] + ticket_duration:
                    next_index += 1

                min_cost = min(min_cost, cost + dfs(next_index))

            self.memo[index] = min_cost
            return min_cost

        return dfs(0)
