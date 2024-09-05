from typing import List

def generateParenthesis(n: int) -> List[str]:
    output = []

    def generate(tmpStr, left, right):
        nonlocal output

        if len(tmpStr) == n * 2:
            output.append(tmpStr)

        if left < n:
            generate(tmpStr + "(", left + 1, right)
        if left > right:
            generate(tmpStr + ")", left, right + 1)

    generate("", 0, 0)
    return output