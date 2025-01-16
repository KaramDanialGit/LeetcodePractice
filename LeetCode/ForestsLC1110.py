class Solution:
    def dfs(self, node, del_set, is_root):
        if not node:
            return

        if node.val in del_set:
            self.dfs(node.left, del_set, True)
            self.dfs(node.right, del_set, True)
        else:
            if node.left:
                if node.left.val in del_set:
                    self.dfs(node.left, del_set, True)
                    node.left = None
                else:
                    self.dfs(node.left, del_set, False)
            if node.right:
                if node.right.val in del_set:
                    self.dfs(node.right, del_set, True)
                    node.right = None
                else:
                    self.dfs(node.right, del_set, False)

            if is_root:
                self.result.append(node)

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        del_set = set(to_delete)
        self.result = []
        self.dfs(root, del_set, True)
        return self.result