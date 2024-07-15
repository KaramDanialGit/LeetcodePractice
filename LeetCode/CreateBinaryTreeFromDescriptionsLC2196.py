def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    graph = {}
    rootSet = set()

    def dfs(node):
        nonlocal graph
        if not node:
            return
        if node.val not in graph:
            return

        if graph[node.val][1]:
            node.left = TreeNode(graph[node.val][1])
        if graph[node.val][0]:
            node.right = TreeNode(graph[node.val][0])

        dfs(node.left)
        dfs(node.right)

    for root, child, isLeft in descriptions:
        rootSet.add(root)
        if root not in graph:
            graph[root] = [None, None]
        graph[root][isLeft] = child

    for _, child, _ in descriptions:
        if child in rootSet:
            rootSet.remove(child)

    rootVal = rootSet.pop()
    root = TreeNode(rootVal)
    dfs(root)
    return root