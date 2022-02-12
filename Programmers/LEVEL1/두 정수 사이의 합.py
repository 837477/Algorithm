def solution(a, b):
    answer = 0
    s, l = (b, a) if a > b else (a, b)
    for i in range(s, l+1):
        answer += i
    return answer