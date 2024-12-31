from typing import List

class Solution:
    def __init__(self):
        self.min_cost = float('inf')

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = [1, 7, 30]

        def dfs(cur_cost, index):
            if index >= len(days):
                return cur_cost

            if cur_cost >= self.min_cost:
                return float('inf')

            min_cost = float('inf')

            cur_idx = index
            while cur_idx < len(days) and days[cur_idx] < days[index] + travel[0]:
                cur_idx += 1
            min_cost = min(min_cost, dfs(cur_cost + costs[0], cur_idx))

            cur_idx = index
            while cur_idx < len(days) and days[cur_idx] < days[index] + travel[1]:
                cur_idx += 1
            min_cost = min(min_cost, dfs(cur_cost + costs[1], cur_idx))

            cur_idx = index
            while cur_idx < len(days) and days[cur_idx] < days[index] + travel[2]:
                cur_idx += 1
            min_cost = min(min_cost, dfs(cur_cost + costs[2], cur_idx))

            return min_cost


        result = dfs(0, 0)

        return result