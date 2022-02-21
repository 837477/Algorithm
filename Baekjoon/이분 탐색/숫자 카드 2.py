from collections import defaultdict
n = int(input())
l = map(int, input().split())
t_n = int(input())
t_l = map(int, input().split())

result = defaultdict(int)
for e in l:
    result[e] += 1
    
for target in t_l:
    print(result[target], end=" ")
