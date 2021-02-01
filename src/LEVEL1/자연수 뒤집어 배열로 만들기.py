def solution(n):
    answer = []
    while n != 0:
        answer += [n%10]
        n //= 10
    return answer

'''
def solution(n):
    answer = []
    for idx, value in enumerate(reversed(str(n))):
        answer.append(int(value))
    return answer
'''