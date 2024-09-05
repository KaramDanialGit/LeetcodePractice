"""
1 A B
2 B C
3 F E
4 F D
5 A D
6 F A

minimum time for everyone to know each other is 5
"""
from collections import defaultdict

def bfs(graph, queue, seen):
    while queue:
        person = queue.pop(0)
        seen.add(person)

        for friend in graph[person]:
            if friend not in seen:
                queue.append(friend)


def getMinFriendIdx(friendRelations):
    graph = defaultdict(list)
    timeLookUp = defaultdict(int)
    totalNames = set()

    for time, f1, f2 in friendRelations:
        totalNames.add(f1)
        totalNames.add(f2)
        timeLookUp[(f1, f2)] = time

    for index, f1, f2 in friendRelations:
        seen = set()
        graph[f1].append(f2)
        graph[f2].append(f1)

        queue = [f1]
        bfs(graph, queue, seen)

        if totalNames == seen:
            return timeLookUp[(f1, f2)]

    return -1


friendRelations = [
    ["1", "A", "B"],
    ["2", "B", "C"],
    ["3", "F", "E"],
    ["4", "F", "D"],
    ["5", "A", "D"],
    ["6", "F", "A"]
]

print(getMinFriendIdx(friendRelations))