def findTheWinner(n: int, k: int) -> int:
    queue = [i for i in range(1, n + 1)]
    index = 0
    size = len(queue)

    while size != 1:
        index = (index + k - 1) % (size)
        queue.pop(index)
        size = len(queue)

    return queue[0]