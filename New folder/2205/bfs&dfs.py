print("DFS Traversal using Adjacency Matrix:")
visited = [False]*len(vertices)

dfs('A',visited)
print("\n")
print("BFS Traversal using Adjacency List:")

bfs('A')
print()

vertices = ['A','B','C','D','E','F']

graph_matrix = [
[0, 1, 1, 0, 0, 0], 
[1, 0, 0, 1, 1, 0], 
[1, 0, 0, 0, 0, 1],
[0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 1],
[0, 0, 1, 0, 1, 0]
]

def dfs(vertex, visited):
    index = vertices.index(vertex)

visited[index] = True
print(vertex, end=" ")

for i in range(len(vertices)):
    if graph_matrix[index][i] == 1 and not visited[i]:
        dfs(vertices[i], visited)

graph_list = {
'A': ['B','C'],
'B': ['A','D','E'],
'C': ['A','F'],
'D': ['B'],
'E': ['B','F'],
'F': ['C','E']
}

def bfs(start):
    visited = set()

queue = []

queue.append(start)
visited.add(start)

while queue:
    vertex = queue.pop(0)
print(vertex, end=" ")

for neighbour in graph_list[vertex]:
    if neighbour not in visited:
        visited.add(neighbour)

queue.append(neighbour)