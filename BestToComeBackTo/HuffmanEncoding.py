import heapq


class Node:
    def __init__(self, value=-1, symbol='', left=None, right=None):
        self.left = left
        self.right = right
        self.symbol = symbol
        self.value = value

    def __lt__(self, nextNode):
        return self.value < nextNode.value


def buildMap(node, val=''):
    if not node:
        return

    if node.symbol:
        print(node.symbol, val)

    buildMap(node.left, val + '0')
    buildMap(node.right, val + '1')


def createHuff(frequency, characters):
    heap = []

    for i in range(len(frequency)):
        heapq.heappush(heap, Node(value=frequency[i], symbol=characters[i]))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        newNode = Node(
            value=(left.value + right.value),
            left=left,
            right=right)

        heapq.heappush(heap, newNode)

    buildMap(heap[0])


freqs = [1, 2, 3, 4]
chars = ['a', 'b', 'c', 'd']
createHuff(freqs, chars)