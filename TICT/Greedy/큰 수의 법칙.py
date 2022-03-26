def my_solution(arr, m, k):
    arr.sort(reverse=True)
    answer = 0
    for i in range(m):
        if i % (k+1) == k:
            answer += arr[1]
        else:
            answer += arr[0]
    return answer


def solution(data, n, m, k):
    data.sort()
    first = data[n-1]
    second = data[n-2]
    answer = 0
    while True:
        for i in range(k):
            if m == 0:
                break
            answer += first
            m -= 1
        if m == 0:
            break
        answer += second
        m -= 1
    return answer


def efficient_solution(data, n, m, k):
    data.sort()
    first = data[n - 1]
    second = data[n - 2]
    count = (int(m/(k+1)) * k) + (m % (k+1))
    return count * first + (m-count) * second


if __name__ == "__main__":
    import sys
    sys.path.insert(1, "../../")
    from testcase import TestCase
    TC = TestCase()

    # 테스트 케이스 입력
    arr = TC.list(int, 1, 5)
    print(my_solution(arr, 8, 3))
    print(solution(arr, 5, 8, 3))
    print(efficient_solution(arr, 5, 8, 3))
