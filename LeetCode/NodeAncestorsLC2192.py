class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Memory limit exceeded by it's my MLE <3
        ancestors = {}

        for start, end in edges:
            if end in ancestors:
                ancestors[end].append(start)
            else:
                ancestors[end] = [start]

        for key in ancestors.keys():
            tmpList = ancestors[key]

            for ancestor in tmpList:
                if ancestor in ancestors:
                    ancestors[key] += ancestors[ancestor]

        result = []

        for i in range(n):
            if i in ancestors:
                result.append(sorted(list(dict.fromkeys(ancestors[i]))))
            else:
                result.append([])

        return result