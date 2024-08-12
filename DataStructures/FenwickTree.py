"""
Design a Fenwick Tree
"""

class FenwickTree:
    def __init__(self, array):
        self.tree = [0]

        for val in array:
            self.tree.append(val)

        for i in range(len(self.tree)):
            parent = i + (i & -i)
            if parent < len(self.tree):
                self.tree[parent] += self.tree[i]

    def query(self, index):
        sumVal = 0

        while index > 0:
            sumVal += self.tree[index]
            index -= (index & -index)

        return sumVal

    def update(self, index, val):
        sumVal = 0

        while index < len(self.tree):
            sumVal[index] += val
            index += (index & -index)

test = [1, 8, 5, 6, 9, 3]

FT = FenwickTree(test)
print(FT.tree)
print(FT.query(5)-FT.query(3))
print(FT.query(3)-FT.query(1))