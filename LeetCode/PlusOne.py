from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1

        while index >= 0:
            if digits[index] == 9:
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                return digits

        if index == -1:
            digits.insert(0, 1)

        return digits