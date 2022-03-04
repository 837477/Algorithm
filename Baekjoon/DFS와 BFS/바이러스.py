from collections import defaultdict, deque


def bfs(graph, now, visited):
    queue = deque()
    queue.append(now)
    visited.append(now)
    answer = -1
    
    while queue:
        v = queue.popleft()
        answer += 1
        for vertex in graph[v]:
            if vertex not in visited:
                queue.append(vertex)
                visited.append(vertex)
    
    return answer

vertexs = int(input())
edges = int(input())
graph = defaultdict(list)
for i in range(edges):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(graph, 1, []))