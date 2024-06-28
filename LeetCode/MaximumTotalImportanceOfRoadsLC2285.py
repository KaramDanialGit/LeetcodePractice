def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
    result = 0
    graph = defaultdict(int)

    for start, end in roads:
        graph[start] += 1
        graph[end] += 1

    ordered_graph = dict(sorted(graph.items(), key=lambda item: item[1], reverse=True))

    for i, j in ordered_graph.items():
        result += j * n
        n -= 1

    return result