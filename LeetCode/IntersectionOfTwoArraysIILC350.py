from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    length = min(len(nums1), len(nums2))

    if length == len(nums1):
        numCounter1 = Counter(nums1)
        numCounter2 = Counter(nums2)
    else:
        numCounter1 = Counter(nums2)
        numCounter2 = Counter(nums1)

    for key, val in numCounter1.items():
        if key in numCounter2:
            iteration = min(numCounter1[key], numCounter2[key])

            for i in range(iteration):
                result.append(key)

    return result