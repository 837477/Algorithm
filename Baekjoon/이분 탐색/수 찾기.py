n = int(input())
l = set(map(int, input().split()))
t_n = int(input())
t_l = list(map(int, input().split()))

for target in t_l:
    print(1) if target in l else print(0)
