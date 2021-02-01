def solution(n):
    t = []
    while True:
        n, m = divmod(n, 3)
        t.append(m)
        if n == 0:
            break
    answer = 0
    for idx, i in enumerate(reversed(t)):
        answer += i * 3**idx
    return answer
