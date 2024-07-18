from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countPairs(root: TreeNode, distance: int) -> int:
    leafs = set()
    visited = set()
    result = 0
    graph = defaultdict(list)

    def generateGraph(node):
        nonlocal graph
        if not node:
            return
        if not node.left and not node.right:
            leafs.add(node.val)

        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            generateGraph(node.left)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            generateGraph(node.right)

    def dfs(i, depth):
        if depth > distance:
            return 0

        if i in leafs:
            return 1

        for node in graph[i]:
            if node not in visited:
                visited.add(node)
                dfs(node, depth + 1)

    generateGraph(root)

    for leaf in leafs:
        result += dfs(leaf, 0)

    return result // 2