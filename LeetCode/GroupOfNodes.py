from typing import List
from collections import defaultdict


# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

# Example 1:
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1

# Create an adj list from edges Input
# Dfs search starting at first node with visited list
# If last node < number of nodes
# Increment number of groups
# repeat dfs on new node

def connected_nodes(edges: List[List[int]]) -> int:
    if not edges:
        return 0

    group = 0
    visited = set()
    adjList = defaultdict(list)

    def dfs(node):
        for neighbor in adjList[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    # Build adj list
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])

    for node in adjList.keys():
        if node not in visited:
            visited.add(node)
            dfs(node)
            group += 1

    return group


assert (connected_nodes([[0, 1], [1, 2], [3, 4]])) == 2
assert (connected_nodes([[0, 1], [1, 2], [2, 3], [3, 4]])) == 1
assert (connected_nodes([[0, 1]])) == 1
assert (connected_nodes([[0, 1], [2, 3], [4, 5]])) == 3

print("All test cases passed my digga!")

# -- With Abel
