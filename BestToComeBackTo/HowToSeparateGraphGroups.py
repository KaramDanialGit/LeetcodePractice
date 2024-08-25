from collections import defaultdict

def dfs(name, graph, visited, curVisited):
    if name in curVisited:
        return curVisited

    visited.add(name)
    curVisited.add(name)

    for relation in graph[name]:
        if relation not in curVisited:
            dfs(relation, graph, visited, curVisited)
    return curVisited

def makeGraph(relations):
    graph = defaultdict(list)
    visited = set()
    groups = []

    for name, friend in relations:
        graph[name].append(friend)
        graph[friend].append(name)

    for name in graph.keys():
        curVisited = set()

        if name not in visited:
            groups.append(dfs(name, graph, visited, curVisited))


    print(graph)
    print(groups)


test = [
    ["Jerry", "Jerri"],
    ["Jary", "Jerri"],
    ["Cori", "Correy"],
    ["Coree", "Correy"]
]

makeGraph(test)