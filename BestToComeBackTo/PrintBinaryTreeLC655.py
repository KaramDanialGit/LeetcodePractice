from typing import List, Optional

class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None

def printTree(root: Optional[TreeNode]) -> List[List[str]]:
    maxHeight = 0

    def getHeight(node):
        if not node:
            return 0

        left = getHeight(node.left) + 1
        right = getHeight(node.right) + 1
        maxHeight = max(left, right)
        return maxHeight

    def dfs(node, result, col, row, maxHeight):
        if not node:
            return

        dfs(node.left, result, col - 2 ** (maxHeight - row - 1), row + 1, maxHeight)
        result[row][(col - 1) // 2] = str(node.val)
        dfs(node.right, result, col + 2 ** (maxHeight - row - 1), row + 1, maxHeight)

    maxHeight = getHeight(root) - 1
    cols = 2 ** (maxHeight + 1) - 1
    rows = maxHeight + 1
    result = [["" for _ in range(cols)] for _ in range(rows)]

    dfs(root, result, cols, 0, maxHeight + 1)

    return result