def solution(n):
    answer = ""
    ott = "124"
    while n != 0:
        n -= 1
        answer = ott[n%3] + answer
        n //= 3
    return answer

if __name__ == "__main__":
    print(solution(6))