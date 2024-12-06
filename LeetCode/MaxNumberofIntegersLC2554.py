
def maxCount(banned List[int], n int, maxSum int) - int
    curSum = 0
    window = []
    banned = set(banned)

    for i in range(1, n + 1)
        if i not in banned
            if curSum + i  maxSum
                break
            else
                curSum += i
                window.append(i)

    return len(window)