## Experiment No. 3: Implement A* Search Algorithm for a Graph

**Name:** MANOJ CHOUDHARY V

**Register Number:** 212221240025

### Aim:
To Implement A* Search Algorithm for a Graph using Python 3.

### Algorithm:

1. Initialize the open list.
2. Initialize the closed list.
   - Put the starting node on the open list (you can leave its f at zero).
3. While the open list is not empty:
   a) Find the node with the least f on the open list, call it "q".
   b) Pop q off the open list.
   c) Generate q's successors and set their parents to q.
   d) For each successor:
      i) If the successor is the goal, stop the search.
      ii) Compute both g and h for the successor.
         - `successor.g = q.g + distance between successor and q`
         - `successor.h = distance from the goal to the successor` (This can be done using various heuristics).
         - `successor.f = successor.g + successor.h`
      iii) If a node with the same position as the successor is in the OPEN list with a lower f than the successor, skip this successor.
      iv) If a node with the same position as the successor is in the CLOSED list with a lower f than the successor, skip this successor; otherwise, add the node to the open list.
   e) Push q on the closed list.

### Program I:
```python
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

```
### Graph I:

![Graph I](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/b1377c3f-011a-4c0f-a843-516842ae056a)


### Output I:
![image](https://github.com/manojvenaram/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/94165064/84a96cfc-1bab-451e-aadb-92920fbde998)

### Program II
``` python
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
n, e = 6, 6

edges = [
    ('A', 'B', 2),
    ('B', 'C', 1),
    ('A', 'E', 3),
    ('B', 'G', 9),
    ('E', 'D', 6),
    ('D', 'G', 1)
]

heuristics = {
    'A': 11,
    'B': 6,
    'C': 99,
    'E': 7,
    'D': 1,
    'G': 0
}

# Initialize the graph
graph = defaultdict(list)

for edge in edges:
    u, v, cost = edge
    graph[u].append((v, float(cost)))
    graph[v].append((u, float(cost)))

H_dist = heuristics

start_node = 'A'  # Replace 'A' with your start node
stop_node = 'G'   # Replace 'G' with your stop node

print('Path found:',aStarAlgo(start_node, stop_node))
```

### Sample Graph II:

![Graph II](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/acbb09cb-ed39-48e5-a59b-2f8d61b978a3)


###  Output II:
![image](https://github.com/manojvenaram/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/94165064/cb00ffbb-d7fe-46b8-914a-1256fa86d089)

## Result:
Thus, a Graph was constructed, and the implementation of the A* algorithm for the same graph was executed successfully. The algorithm found the shortest path from the start node to the stop node, demonstrating its effectiveness in solving pathfinding problems.
