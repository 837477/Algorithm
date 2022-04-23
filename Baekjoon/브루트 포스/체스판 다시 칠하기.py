n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

result = []
for si in range(n-7):
    for sj in range(m-7):
        w = 0
        b = 0
        for i in range(si, si+8):
            for j in range(sj, sj+8):
                if (i + j) % 2 == 0:
                    if chess[i][j] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if chess[i][j] != 'B':
                        w += 1
                    else:
                        b += 1
        result.append(min(w, b))
print(min(result))