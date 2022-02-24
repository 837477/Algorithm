n = int(input())
meetings = [list(map(int, input().split())) for i in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

prev = meetings[0]
result = 1
for i in range(1, n):
    if prev[1] <= meetings[i][0]:
        prev = meetings[i]
        result += 1
    else:
        continue

print(result)
