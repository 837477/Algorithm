def b_s(lans, n, start, end):
    if start > end:
        return end

    mid = (start + end) // 2
    _sum = 0
    for lan in lans:
        _sum += lan // mid

    elif _sum < n:
        return b_s(lans, n, start, mid-1)
    else:
        return b_s(lans, n, mid+1, end)
    
k, n = map(int, input().split())
lans = [int(input()) for i in range(k)]
start, end = 1, max(lans)
print(b_s(lans, n, start, end))
