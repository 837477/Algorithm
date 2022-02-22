n = int(input())
l = list(map(int, input().split()))
result = [l[0]]

def b_s(start, end, target):
    if start > end:
        return start

    mid = (start + end) // 2

    if result[mid] < target:
        return b_s(mid+1, end, target)
    else:
        return b_s(start, mid-1, target) 

for i in l:
    if result[-1] < i:
        result.append(i)
    else:    
        result[b_s(0, len(result) - 1, i)] = i

print(len(result))
