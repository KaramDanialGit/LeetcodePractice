import math


def solve(A, B, n, c):
    c.sort()
    for i in range(n - 1):
        fights = math.ceil(c[i][1] / A)
        B -= c[i][0] * fights
        if B <= 0:
            return "NO"

    fights = math.ceil(c[n - 1][1] / A)
    if B - c[n - 1][0] * (fights - 1) > 0:
        return "YES"
    else:
        return "NO"


test_cases = int(input())
for _ in range(test_cases):
    A, B, n = list(map(int, input().split()))
    c = []
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        c.append([a[i], b[i]])
    print(solve(A, B, n, c))