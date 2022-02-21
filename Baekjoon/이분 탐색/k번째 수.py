n = int(input())
k = int(input())
"""
[
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]
"""

def b_s(start, end, target):
    if start > end:
        return start

    mid = (start + end) // 2 # 5 -> 7

    cnt = 0
    for i in range(1, n+1): # 1~3
        cnt += min(mid//i, n) # 5, 3! / 2!, 3 / 1!, 3 -> 7, 3! / 3!, 3 / 2!, 3

    if cnt < target: # 6, 7
        return b_s(mid+1, end, target) # 6, 9
    else:
        return b_s(start, mid-1, target) 

print(b_s(1, n*n, k))
