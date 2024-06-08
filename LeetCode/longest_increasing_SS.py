def longest_increases_ss(A):
    L = [1] * len(A)

    for i in range(1, len(A)):
        problem = [L[k] for k in range(i) if A[k] < A[i]]
        L[i] = 1 + max(problem, default=0)

    return max(L, default=0)


test = [5, 2, 8, 6, 3, 6, 9, 5]
print(longest_increases_ss(test))
