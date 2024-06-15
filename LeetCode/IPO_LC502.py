def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    minHeap = []
    revArr = []
    n = len(profits)
    currentCapital = w

    for i in range(n):
        revArr.append((capital[i], profits[i]))
    revArr.sort()

    i = 0

    while k:
        while i < n and revArr[i][0] <= currentCapital:
            heapq.heappush(minHeap, -revArr[i][1])
            i += 1

        if minHeap:
            currentCapital += -heapq.heappop(minHeap)
        k -= 1

    return currentCapital