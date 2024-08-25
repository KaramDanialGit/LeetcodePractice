"""
Given a set of nodes specifying their connections through from and to arrays, determine which node causes the most infection
and requires removal. If two or more nodes infect the same number of nodes, return the node with the lowest value.
"""

from collections import defaultdict
from copy import deepcopy

def maxInfector(num_nodes, node_from, node_to, infected):
    graph = defaultdict(list)
    infected_queue = []
    number_node_infects = [0] * (num_nodes + 1)

    for node, neighbor in zip(node_from, node_to):
        graph[node].append(neighbor)
        graph[neighbor].append(node)

    for i in range(0, num_nodes):
        if infected[i] == 1 and i not in infected_queue:
            infected_queue.append(i + 1)

    while infected_queue:
        visited = set()

        current_num_infected = 0
        current_infected = [infected_queue.pop(0)]
        index = deepcopy(current_infected[0])

        while current_infected:


            current = current_infected.pop(0)

            if infected[current - 1] == 0:
                current_num_infected += 1

            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    current_infected.append(neighbor)

        number_node_infects[index] = current_num_infected

    maxInfected = max(number_node_infects)
    print(number_node_infects.index(maxInfected))

g_nodes = 6
g_from = [1, 3, 4, 1]
g_to = [2, 2, 5, 6]
# Node 1, 3, 5 are infected
g_infected = [1, 0, 1, 0, 1, 0]

maxInfector(g_nodes, g_from, g_to, g_infected)