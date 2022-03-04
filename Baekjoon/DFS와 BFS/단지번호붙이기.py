range_x = [-1, 1, 0, 0]
range_y = [0, 0, -1, 1]
def is_range(x, y):
    global n
    return True if x < 0 or x >= n or y < 0 or y >= n else False

def dfs(graph, now):
    if (is_range(now[0], now[1])
        or graph[now[0]][now[1]] == 0):
        return
    global cnt
    cnt += 1
    graph[now[0]][now[1]] = 0
    for i in range(4):
        dfs(graph, [now[0] + range_x[i], now[1] + range_y[i]])


n = int(input())
graph = [list(map(int, list(input()))) for i in range(n)]
answer = []

for i in range(n):
    for j in range(n):
        cnt = 0
        dfs(graph, [i, j])
        if cnt > 0:
            answer.append(cnt)

answer.sort()
print(len(answer))
for value in answer:
    print(value)