def solution(a, b):
    answer = 0
    if a > b:
        s = b
        l = a
    else:
        s = a
        l = b
    for i in range(s, l+1):
        answer += i
    return answer