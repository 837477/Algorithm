def backtracking(s, n, m):
    global print_
    if m == 0:
        for p in print_:
            print(p, end=" ")
        print()
        return

    for i in range(s, n+1):
        print_.append(i)
        backtracking(i, n, m-1)
        print_.pop()
            

n, m = list(map(int, input().split()))

# backtracking 방식
print_ = []
backtracking(1, n, m)
