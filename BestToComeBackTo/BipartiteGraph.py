from collections import defaultdict

def is_bipartite(adj_matrix):
    graph = defaultdict(list)

    for start, end in adj_matrix:
        graph[start].append(end)
        graph[end].append(start)

    nodes = len(list(graph.keys()))
    colors = [-1] * (nodes + 1)

    color = 1
    queue = [1]
    colors[1] = color
    visited = set()

    while queue:
        current = queue.pop(0)
        visited.add(current)
        color = 0 if color == 1 else 1

        for neighbor in graph[current]:
            if colors[neighbor] == colors[current]:
                return False

        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            else:
                queue.append(neighbor)
                colors[neighbor] = color

    return True

adj_list = [[1,2], [1,3], [1,4]]
print(is_bipartite(adj_list))