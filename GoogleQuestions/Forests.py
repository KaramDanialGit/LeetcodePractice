"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Example 1:
Input: root = [1,2,3], to_delete = [1]
Output: [[2],[3]]

Example 2:
Input: root = [1,2,3,4], to_delete = [4]
Output: [[1,2,3,null]]

Example 3:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

1. Return the shortest tree in the forest.

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lumber_jack(root, delete):
    if not root:
        return []

    def solve(node, array, seen):
        if not node:
            return

        temp = []
        queue = [node]

        while queue:
            current = queue.pop(0)

            if current.val in delete:
                if current.left:
                    solve(current.left, array, seen)
                if current.right:
                    solve(current.right, array, seen)
            else:
                if current.val not in seen:
                    temp.append(current.val)
                    seen.add(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        array.append(temp)

    result = []
    visited = set()
    solve(root, result, visited)
    print(result)
    return result


# Example 3:
# [1,2,3,4,5,6,7]
forest = TreeNode(1)
forest.left = TreeNode(2)
forest.right = TreeNode(3)
forest.left.left = TreeNode(4)
forest.left.right = TreeNode(5)
forest.right.left = TreeNode(6)
forest.right.right = TreeNode(7)

to_delete = set([3, 5])
lumber_jack(forest, to_delete)
