def backtracking(target, visited, m, len_):
    global print_, overlap
    cnt = 0
    for check in visited:
        if check:
            cnt += 1
    if cnt == m:
        if set(print_) not in overlap:
            for p in print_:
                print(p, end=" ")
            print()
            overlap.append(set(print_))
        return

    for i in range(len_):
        if not visited[i]: # 방문을 안했을 때,
            print_.append(target[i])
            visited[i] = True
            backtracking(target, visited, m, len_)
            print_.pop()
            visited[i] = False
    
            

n, m = list(map(int, input().split()))

# backtracking 방식
overlap = []
print_ = []
visited = [False for i in range(n)]
target = [i for i in range(1, n+1)]
backtracking(target, visited, m, n)

