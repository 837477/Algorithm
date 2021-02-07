def solution(n):
    answer = 0
    for i in range(1, n//2 + 1):
        cnt = 0
        for j in range(i, n):
            cnt += j
            if cnt > n:
                break
            if cnt == n:
                answer += 1
                break
    return answer + 1

if __name__ == "__main__":
    print(solution(15))

'''
15 // 2 = 7

'''