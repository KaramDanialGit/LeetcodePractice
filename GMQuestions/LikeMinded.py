from typing import List
from collections import defaultdict

def isPath(graph, name, similar):
    visited1, visited2 = set(), set()

    if dfs(graph, name, visited1) == dfs(graph, similar, visited2):
        return True

    return False

def dfs(graph, name, visited):
    if name in visited:
        return visited

    visited.add(name)

    for child in graph[name]:
        if child not in visited:
            dfs(graph, child, visited)

    return visited

def determineSimilarNameFreq(nameNumbers, similarNames):
    graph = defaultdict(list)
    result = defaultdict(int)

    for name, similar in similarNames:
        graph[name].append(similar)
        graph[similar].append(name)

    visitedIdx = set()

    for i in range(len(nameNumbers)):
        if i in visitedIdx:
            continue

        for j in range(i + 1, len(nameNumbers)):
            if isPath(graph, nameNumbers[i][0], nameNumbers[j][0]):
                visitedIdx.add(j)
                nameNumbers[j][0] = nameNumbers[i][0]

    for name, freq in nameNumbers:
        result[name] += freq

    return list(result.items())


numberOfNames = [
    ["Lucian", 10],
    ["Lushan", 2],
    ["Lucan", 2],
    ["Velma", 3],
    ["Velmah", 1],
    ["Vilma", 13],
    ["Will", 21]
]

similarNames = [
    ["Lucian", "Lucan"],
    ["Lushan", "Lucian"],
    ["Velma", "Velmah"],
    ["Vilma", "Velma"]
]

print(determineSimilarNameFreq(numberOfNames, similarNames))