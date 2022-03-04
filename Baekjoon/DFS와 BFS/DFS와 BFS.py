from collections import defaultdict, deque


def dfs(graph, now, visited):
    if now in visited:
        return
    print(now, end=' ')
    visited.append(now)
    for vertex in graph[now]:
        dfs(graph, vertex, visited)


def bfs(graph, now, visited):
    queue = deque()
    queue.append(now)
    visited.append(now)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for vertex in graph[v]:
            if vertex not in visited:
                queue.append(vertex)
                visited.append(vertex)


vertexs, edges, start = map(int, input().split())
graph = defaultdict(list)
for i in range(edges):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for vertex in graph:
    graph[vertex].sort()

dfs(graph, start, [])
print()
bfs(graph, start, [])

