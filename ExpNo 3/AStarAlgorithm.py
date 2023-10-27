from collections import defaultdict

H_dist = {}

def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {node: float('inf') for node in graph}
    g[start_node] = 0
    parents = {node: None for node in graph}
    parents[start_node] = start_node

    while open_set:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            # print('Path found:', path)
            return path

        open_set.remove(n)
        closed_set.add(n)

        for m, weight in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

    print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in graph:
        return graph[v]
    else:
        return []

def heuristic(n):
    return H_dist[n]

# Predefined input data
n, e = 10, 14

edges = [
    ('A', 'B', 6),
    ('A', 'F', 3),
    ('B', 'D', 2),
    ('B', 'C', 3),
    ('C', 'D', 1),
    ('C', 'E', 5),
    ('D', 'E', 8),
    ('E', 'I', 5),
    ('E', 'J', 5),
    ('F', 'G', 1),
    ('G', 'I', 3),
    ('I', 'J', 3),
    ('F', 'H', 7),
    ('I', 'H', 2)
]

heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

for edge in edges:
    u, v, cost = edge
    graph[u].append((v, float(cost)))
    graph[v].append((u, float(cost)))

H_dist = heuristics

start_node = 'A'  # Replace 'A' with your start node
stop_node = 'J'   # Replace 'J' with your stop node

print("Path Found :",aStarAlgo(start_node, stop_node))
