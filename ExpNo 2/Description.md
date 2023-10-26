## Experiment No. 2: Implement Breadth First Search Traversal of a Graph

**Name:** Manoj Choudhary V

**Register Number** 212221240025 

### Aim:
To Implement Breadth First Search Traversal of a Graph using Python 3.

### Theory:
Breadth-First Traversal (BFS) for a graph is similar to BFS for a tree but can handle cycles. It divides vertices into two categories: Visited and Not Visited. A Boolean visited array marks visited vertices, and BFS uses a queue data structure for traversal.

**How BFS Works:**
- Starting from the root, all the nodes at a particular level are visited first, and then the next level nodes are traversed until all the nodes are visited.
- A queue is used. All the adjacent unvisited nodes of the current level are pushed into the queue, and the current-level nodes are marked visited and popped from the queue.

### Algorithm:
1. Construct a Graph with Nodes and Edges.
2. BFS Uses a Queue and iterates through the Queue for Traversal.
3. Insert a Start Node into the Queue.
4. Find its Successors or neighbors and check whether the node is visited or not.
5. If not visited, add it to the Queue; otherwise, continue.
6. Iterate steps 4 and 5 until all nodes get visited, and there are no more unvisited nodes.

### Program
```python
from collections import deque
from collections import defaultdict
def bfs(graph,start,visited,path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        tmpnode = queue.popleft()
        for neighbour in graph[tmpnode]:
            if visited[neighbour] == False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path

graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

start = '0'
path = []
visited = defaultdict(bool)
traversedpath = bfs(graph,start,visited,path)
print(traversedpath)
```

### Sample Input
```
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
```

### Sample Output
```
['A', 'B', 'C', 'F', 'E', 'D', 'G']
```

### Sample Input
```
5 6
0 1
0 2
1 2
1 3
2 4
3 4
```

### Sample Output
```
['0', '1', '2', '3', '4']
```

### Result:
Thus, a graph was constructed, and the implementation of Breadth First Search for the same graph was done successfully.
