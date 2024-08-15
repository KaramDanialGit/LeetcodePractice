class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root: TreeNode) -> TreeNode:
    inorder = []

    def dfs(root, newArr):
        if not root:
            return

        dfs(root.left, newArr)
        newArr.append(root.val)
        dfs(root.right, newArr)

    def reconstruct(array, left, right):
        if left > right:
            return None

        middle = left + (right - left) // 2

        newNode = TreeNode(array[middle])
        newNode.left = reconstruct(array, left, middle - 1)
        newNode.right = reconstruct(array, middle + 1, right)

        return newNode

    dfs(root, inorder)
    newTree = reconstruct(inorder, 0, len(inorder) - 1)

    return newTree