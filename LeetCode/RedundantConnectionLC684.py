from typing import List

class DSU:
    def __init__(self, N):
        self.degree = [1] * N
        self.parent = [i for i in range(N)]

    def _find(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]

    def _union(self, n1, n2):
        n1 = self._find(n1)
        n2 = self._find(n2)

        if n1 == n2:
            return False
        else:
            if self.degree[n1] > self.degree[n2]:
                self.parent[n2] = n1
                self.degree[n1] += self.degree[n2]
            else:
                self.parent[n1] = n2
                self.degree[n2] += self.degree[n1]
            return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        dsu = DSU(N)
        for start, end in edges:
            if not dsu._union(start - 1, end - 1):
                return [start, end]

        return []