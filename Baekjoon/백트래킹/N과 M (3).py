def backtracking(n, m):
    global print_
    if m == 0:
        for p in print_:
            print(p, end=" ")
        print()
        return

    for i in range(1, n+1):
        print_.append(i)
        backtracking(n, m-1)
        print_.pop()
            

n, m = list(map(int, input().split()))

# backtracking 방식
print_ = []
backtracking(n, m)
