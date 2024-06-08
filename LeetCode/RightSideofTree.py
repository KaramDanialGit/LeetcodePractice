# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]


# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]


# Example 3:

# Input: root = []
# Output: []

def ISpyRightNode(root: TreeNode) -> list[int]:
    result = []
    queue = [(root, 1)]
    current = None
    depth = 0

    last_depth, last_value = 1, root.val

    while queue:
        current, depth = queue.pop(0)

        if (last_depth != depth):
            result.append(last_value)

        last_depth, last_value = depth, current.val

        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))

    result.append(current.val)
    print(result)


test_root = TreeNode(1)
test_root.left = TreeNode(2)
test_root.right = TreeNode(3)
test_root.left.right = TreeNode(5)
test_root.right.right = TreeNode(4)

ISpyRightNode(test_root)