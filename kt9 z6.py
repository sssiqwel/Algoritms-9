k = 3
values = [1, -2, 3, 4, -1]
edges = [
    (1, 2),
    (1, 3),
    (3, 4),
    (3, 5),
]
n = len(values)
NEG = -10 ** 30

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

best = [[NEG] * (k + 1) for _ in range(n)]
size = [1] * n
for vertex in reversed(order):
    best[vertex][1] = values[vertex]
    for nxt in graph[vertex]:
        if nxt == parent[vertex]:
            continue
        merged = [NEG] * (k + 1)
        for taken in range(1, size[vertex] + 1):
            if best[vertex][taken] <= NEG // 2:
                continue
            merged[taken] = max(merged[taken], best[vertex][taken])
            for extra in range(1, size[nxt] + 1):
                if taken + extra > k or best[nxt][extra] <= NEG // 2:
                    continue
                merged[taken + extra] = max(
                    merged[taken + extra],
                    best[vertex][taken] + best[nxt][extra],
                )
        best[vertex] = merged
        size[vertex] = min(k, size[vertex] + size[nxt])

answer = NEG
for vertex in range(n):
    answer = max(answer, best[vertex][k])
print(answer)
