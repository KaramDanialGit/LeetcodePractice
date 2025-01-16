from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        prevChar = ""
        curCount = 0

        for char in chars:
            if prevChar == "":
                prevChar = char
                curCount += 1
                continue

            if prevChar != char:
                result.append(prevChar)
                if curCount > 1:
                    for val in str(curCount):
                        result.append(val)
                prevChar = char
                curCount = 1
            else:
                curCount += 1

        result.append(prevChar)
        if curCount > 1:
            for val in str(curCount):
                result.append(val)

        for i, x in enumerate(result):
            chars[i] = x

        for i in range(len(chars) - len(result)):
            chars.pop()

        return len(result)