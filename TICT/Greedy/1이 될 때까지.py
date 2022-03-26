def my_solution(n, k):
    answer = 0
    cnt = 0
    while n != 1:
        cnt += 1
        if n % k == 0:
            n //= k
        else:
            n -= 1
        answer += 1
    return answer, cnt


def efficient_solution(n, k):
    answer = 0
    cnt = 0
    while True:
        cnt += 1
        # n이 k로 나누어 떨어지는 수가 될 때까지 1씩 뺀 횟수 구하기
        answer += n % k
        n = (n // k) * k # == n - (n%k)

        # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break

        answer += 1
        n //= k
    answer += (n - 1)
    return answer, cnt


if __name__ == "__main__":
    import sys
    sys.path.insert(1, "../../")
    from testcase import TestCase
    TC = TestCase()

    # 테스트 케이스 입력
    n = TC.int(20000, zero=False)
    k = TC.int(1, zero=False)
    print(n, k)

    import time
    start = time.time()
    print(my_solution(n, k))
    print(time.time() - start)

    start = time.time()
    print(efficient_solution(n, k))
    print(time.time() - start)
