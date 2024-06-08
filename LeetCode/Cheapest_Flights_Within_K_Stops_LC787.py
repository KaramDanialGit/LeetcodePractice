from typing import List
from collections import defaultdict


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj_flights = defaultdict(list)
    costs = defaultdict(list)

    for flight in flights:
        adj_flights[flight[0]].append(flight[1])
        costs[(flight[0], flight[1])] = flight[2]

    def dfs(start, end, memo):
        if start == dst:
            return 0

        if end < 0:
            return float('inf')

        if (start, end) in memo:
            return memo[(start, end)]

        min_result = float('inf')

        for neighbor in adj_flights[start]:
            result = dfs(neighbor, end - 1, memo) + costs[(start, neighbor)]
            min_result = min(result, min_result)

        memo[(start, end)] = min_result
        return min_result

    memo = {}
    cost = dfs(src, k, memo)
    return -1 if cost == float('inf') else cost


x = findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3, k=1)
assert x == 700
