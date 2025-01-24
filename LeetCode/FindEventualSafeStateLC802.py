from typing import List
from Collections import defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = defaultdict(list)

        for node, neighbours in enumerate(graph):
            for neighbour in neighbours:
                adj[neighbour].append(node)
                indegree[node] += 1

        queue = []

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        safe = [False] * n
        while queue:
            node = queue.pop(0)
            safe[node] = True

            for neighbour in adj[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        result = []
        for i in range(n):
            if safe[i] == True:
                result.append(i)

        return result