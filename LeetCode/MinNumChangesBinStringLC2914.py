
def minChanges(s: str) -> int:
    minFlips = 0
    n = len(s)

    for i in range(0, n, 2):
        if s[i] != s[i + 1]:
            minFlips += 1

    return minFlips