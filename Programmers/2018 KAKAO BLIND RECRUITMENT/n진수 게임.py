def converter(n, base):
    C = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return C[r]
    else:
        return converter(q, base) + C[r]

def solution(n, t, m, p):
    answer = ''
    num = 0
    temp = converter(num, n) # '0' len(temp) -> 1
    idx = 0
    while(len(answer) != t):
        if len(temp) <= idx:
            num += 1
            temp += converter(num, n)
        if idx + 1 == p:
            answer += temp[idx]
            p += m
        idx += 1
    return answer
    
if __name__ == "__main__":
    print(solution(16, 16, 2, 1))
    
    
'''
0 1 10 11 100
101
110
111
'''