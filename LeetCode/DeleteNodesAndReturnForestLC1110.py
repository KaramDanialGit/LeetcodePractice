from typing import List, Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def delNodes(root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    result = []
    delete = set(to_delete)

    if root.val not in delete:
        result.append(root)

    def dfs(node):
        nonlocal delete
        if not node:
            return

        if node.left:
            dfs(node.left)
            if node.left.val in delete:
                node.left = None
        if node.right:
            dfs(node.right)
            if node.right.val in delete:
                node.right = None

        if node.val in delete:
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)

    dfs(root)
    return result
