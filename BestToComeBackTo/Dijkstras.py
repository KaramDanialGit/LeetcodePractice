import heapq

def dijkstras(start, end, adj_list, num_nodes):
    distances = [10**9 for _ in range(num_nodes)]
    distances[start] = 0
    graph = {}

    for node, neighbour, weight in adj_list:
        if node not in graph:
            graph[node] = {}
        if neighbour not in graph:
            graph[neighbour] = {}
        graph[node][neighbour] = weight
        graph[neighbour][node] = weight

    pq = [(0, start)]
    heapq.heapify(pq)
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node not in visited:
            visited.add(current_node)

            for neighbour, weight in graph[current_node].items():
                tentative_distance = current_dist + weight
                if tentative_distance < distances[neighbour]:
                    distances[neighbour] = tentative_distance
                    heapq.heappush(pq, (tentative_distance, neighbour))

    print(distances)
    return distances[end]
        

adj_matrix = [
    [0, 1, 2],
    [0, 2, 6],
    [1, 3, 5],
    [2, 3, 8],
    [3, 5, 15],
    [3, 4, 10],
    [5, 4, 6],
    [4, 6, 2],
    [5, 6, 6]
]

beginning = 0
dest = 6
num_nodes = 7

dijkstras(beginning, dest, adj_matrix, num_nodes)
