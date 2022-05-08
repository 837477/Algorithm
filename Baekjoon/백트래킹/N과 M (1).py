from itertools import permutations


def backtracking(target, visited, m, len_):
    global print_
    cnt = 0
    for check in visited:
        if check:
            cnt += 1
    if cnt == m:
        for p in print_:
            print(p, end=" ")
        print()
        return

    for i in range(len_):
        if not visited[i]: # 방문을 안했을 때,
            print_.append(target[i])
            visited[i] = True
            backtracking(target, visited, m, len_)
            print_.pop()
            visited[i] = False
    

def backtracking2(n, m):
    global print_
    if m == 0:
        for p in print_:
            print(p, end=" ")
        print()
        return

    for i in range(1, n+1):
        if i not in print_:
            print_.append(i)
            backtracking2(n, m-1)
            print_.pop()

n, m = list(map(int, input().split()))

# permutations 방식
# for occation in permutations([i for i in range(1, n+1)], m):
#     for value in occation:
#         print(value, end=" ")
#     print()

# backtracking 방식
print_ = []
visited = [False for i in range(n)]
target = [i for i in range(1, n+1)]
# backtracking(target, visited, m, n)

backtracking2(n, m)

