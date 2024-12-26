from typing import List

class Solution:
    def __init__(self):
        self.total = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def backtrack(path, current, index):
            if index == len(nums):
                if current == target:
                    self.total += 1
            else:
                path.append(index)

                backtrack(path, current + nums[index], index + 1)
                backtrack(path, current - nums[index], index + 1)

        backtrack([], 0, 0)
        return self.total