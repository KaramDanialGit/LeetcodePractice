class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []

        def dfs(index, path):
            if sum(path) > target or index >= len(candidates):
                return
            if sum(path) == target:
                self.result.append(path[:])
                return

            path.append(candidates[index])

            dfs(index, path)
            path.pop()
            dfs(index + 1, path)

        dfs(0, [])
        return self.result
