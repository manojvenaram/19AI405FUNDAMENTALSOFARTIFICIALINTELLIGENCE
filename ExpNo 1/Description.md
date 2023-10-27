## ExpNo 1: Implement Depth First Search Traversal of a Graph
### Name: Manoj Choudhary V
### Register Number: 212221240025
### Aim:
To Implement Depth First Search Traversal of a Graph using Python 3.

### Theory:
**Depth First Traversal (DFS)** for a graph is like Depth First Traversal of a tree. The only catch here is that, unlike trees, graphs may contain cycles (a node may be visited twice). Use a Boolean visited array to avoid processing a node more than once. A graph can have more than one DFS traversal.

Depth-first search is an algorithm for traversing or searching trees or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

### Algorithm:
1. Construct a Graph with Nodes and Edges
2. Depth First Search Uses Stack and Recursion
3. Insert a START node to the STACK
4. Find its Successors Or neighbors and Check whether the node is visited or not
5. If Not Visited, add it to the STACK. Else Call The Function Again Until No more nodes need to be visited.

### Program I:
```python
Developed By Manoj Choudhary V
Reg No: 212221240025
from collections import defaultdict
def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if visited[neighbour] == False:
            dfs(graph, neighbour, visited, path)
            visited[neighbour] = True
    return path
graph = defaultdict(list)
n, e = map(int, input().split())
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)
start = 'A'
visited = defaultdict(bool)
path = []
traversedpath = dfs(graph, start, visited, path)
print(traversedpath)
```
## Output I
![image](https://github.com/manojvenaram/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/94165064/a33d49a8-eff9-4809-bf71-f5d8a17a62f1)

### Program II:
```python
Developed By Manoj Choudhary V
Reg No: 212221240025
from collections import defaultdict
def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if visited[neighbour] == False:
            dfs(graph, neighbour, visited, path)
            visited[neighbour] = True
    return path
graph = defaultdict(list)
n, e = map(int, input().split())
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)
start = '0'
visited = defaultdict(bool)
path = []
traversedpath = dfs(graph, start, visited, path)
print(traversedpath)
```
## Output II
![image](https://github.com/manojvenaram/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/94165064/b44bde7e-3276-4cd1-9a00-48fa500a69be)

### Result:
Thus, a Graph was constructed, and the implementation of Depth First Search for the same graph was done successfully.
