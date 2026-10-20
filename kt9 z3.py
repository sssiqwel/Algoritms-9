values = [3, 2, 1, 4]
edges = [
    (1, 2),
    (1, 3),
    (3, 4),
]
n = len(values)

graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

parent = [-1] * n
order = []
stack = [0]
parent[0] = 0
while stack:
    vertex = stack.pop()
    order.append(vertex)
    for nxt in graph[vertex]:
        if nxt == parent[vertex]:
            continue
        parent[nxt] = vertex
        stack.append(nxt)

take = [0] * n
skip = [0] * n
for vertex in reversed(order):
    take[vertex] = values[vertex]
    skip[vertex] = 0
    for nxt in graph[vertex]:
        if nxt == parent[vertex]:
            continue
        take[vertex] += skip[nxt]
        skip[vertex] += max(take[nxt], skip[nxt])

print(max(take[0], skip[0]))
