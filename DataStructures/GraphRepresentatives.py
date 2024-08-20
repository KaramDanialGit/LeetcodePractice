
def dfs(start, visited, graph):
    if start in visited:
        return

    visited.add(start)

    for val in graph[start]:
        if val not in visited:
            dfs(val, visited, graph)

def isValidPath(start, end, graph):
    visited1 = set()
    visited2 = set()

    dfs(start, visited1, graph)
    dfs(end, visited2, graph)

    if end in visited1 and start in visited2:
        return True
    return False

def compressGraph(adjList):
    graph = {}

    for start, end in adjList:
        if start not in graph:
            graph[start] = [end]
            graph[end] = []
        else:
            graph[start].append(end)

    parents = list(graph.keys())
    index1 = 0
    index2 = 1

    while index1 < len(parents) and index2 < len(parents):
        if isValidPath(parents[index1], parents[index2], graph) and isValidPath(parents[index2], parents[index1], graph):
            parents[index2] = parents[index1]
        index2 += 1

        if index2 == len(parents):
            index1 += 1
            index2 = index1 + 1
    print(list(zip(graph.keys(), parents)))

adjList = [[1, 2], [1, 4], [2, 3], [3, 4], [4, 2]]
print(compressGraph(adjList))