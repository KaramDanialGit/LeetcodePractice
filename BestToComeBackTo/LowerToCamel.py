"""
You're responsible for fixing code using snake_case naming conventions in your code base to camelCase. If you
are guaranteed only one _ in between words, write an algorithm to convert lower case variable names to camelCase.
Note, words leading or ending with any number of underscores should be preserved within the string.

E.g. "This code base uses __camel_case" => "This code base uses __camelCase"
"""

def solution(src):
    length = len(src)

    for i in range(1, length - 1):
        if i >= len(src):
            break

        if src[i] == "_":
            if i + 1 < len(src) and i - 1 >= 0:
                if src[i + 1].isalpha() and src[i - 1].isalpha():
                    capital = src[i + 1].upper()
                    tmp = src[:i] + capital

                    if i + 2 < len(src):
                        tmp += src[i + 2:]
                    src = tmp

    return src