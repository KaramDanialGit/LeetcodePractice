
class DisjointSet:
    def __init__(self, size):
        self.rank = [1] * size
        self.parent = [i for i in range(size)]

    def find(self, value):
        if value != self.parent[value]:
            self.parent[value] = self.find(self.parent[value])

        return self.parent[value]

    def union(self, value1, value2):
        findP1 = self.find(value1)
        findP2 = self.find(value2)

        if findP1 == findP2:
            return

        if self.rank[findP1] < self.rank[findP2]:
            self.parent[findP1] = self.parent[findP2]
            self.rank[findP2] += 1
        else:
            self.parent[findP2] = self.parent[findP1]
            self.rank[findP1] += 1
