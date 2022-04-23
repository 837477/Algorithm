n = int(input())
result = 0
for i in range(n):
    if sum(map(int, list(str(i)))) + i == n:
        result = i
        break
print(result)
