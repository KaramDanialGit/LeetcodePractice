from typing import List

def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    maxLen = 0

    for num in numSet:
        if num - 1 not in numSet:
            curNum = num
            longestSeq = 1

            while curNum in numSet:
                maxLen = max(longestSeq, maxLen)
                curNum += 1
                longestSeq += 1

    return maxLen