n = int(input())
roads = list(map(int, input().split()))
stations = list(map(int, input().split()))

result = 0
_min = stations[0]
km = roads[0]
for i in range(1, n-1):
    if _min > stations[i]:
        result += _min * km
        km = roads[i] # 2
        _min = stations[i] # 2
    else:
        km += roads[i] # 5

    if i == n-2:
        result += _min * km

print(result)