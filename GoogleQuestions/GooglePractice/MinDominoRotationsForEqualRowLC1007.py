def minRotations(A, B):
    length = len(A)

    def check(x):
        rotA, rotB = 0, 0

        for i in range(length):
            if A[i] != x and B[i] != x:
                return -1
            elif A[i] != x:
                rotA += 1
            elif B[i] != x:
                rotB += 1
        return min(rotA, rotB)

    result = check(A[0])
    if result != -1 or A[0] == B[0]:
        return result
    else:
        return check(B[0])


tops = [2,1,2,4,2,2]
bots = [5,2,6,2,3,2]
print(minRotations(tops, bots))