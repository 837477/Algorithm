def my_solution(arr):
    arr.sort(key=lambda x:min(x), reverse=True)
    return min(arr[0])


if __name__ == "__main__":
    import sys
    sys.path.insert(1, "../../")
    from testcase import TestCase
    TC = TestCase()

    # 테스트 케이스 입력
    n = 3
    m = 3
    # arr = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
    arr = [TC.list(int, 1, m) for _ in range(n)]
    print(arr)
    print(my_solution(arr, n, m))
