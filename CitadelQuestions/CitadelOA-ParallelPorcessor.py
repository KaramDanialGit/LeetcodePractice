# Given a set of jobs a processor wants to complete in parallel each with an associated
# execution time, solve for the minimum amount of operations required to complete all jobs
# If the main job chosen for that operation decrements x units while the remaining jobs lose
# y execution time (y < x).

# Example: n=5, executionTime=[3,4,1,7,6], x=4, y=2
# Output: 3 operations

import heapq

def parallelProcessor(executionTime, x, y) -> int:
    operations = 0

    heap = []
    for val in executionTime:
        heapq.heappush(heap, -1 * val)

    while heap:
        maxJob = -1 * heapq.heappop(heap)
        maxJob -= x

        for _ in heap:
            tmp = -1 * heapq.heappop(heap)
            tmp -= y
            if tmp > 0:
                heapq.heappush(heap, -1 * tmp)

        if maxJob > 0:
            heapq.heappush(heap, -1 * maxJob)

        operations += 1

    return operations


execTime = [3,4,1,7,6]
X = 4
Y = 2
print(parallelProcessor(execTime, X, Y))