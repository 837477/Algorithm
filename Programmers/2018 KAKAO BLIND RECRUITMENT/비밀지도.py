def binary(num, l):
    result = bin(num)[2:]
    while len(result) != l:
        result = "0" + result
    return result

def summatrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def solution(n, arr1, arr2):
    map1 = [list(map(int, list(binary(i, n)))) for i in arr1]
    map2 = [list(map(int, list(binary(i, n)))) for i in arr2]

    sm = summatrix(map1, map2)

    answer = []
    for m in sm:
        temp = ""
        for i in m:
            temp += '#' if i > 0 else ' '
        answer.append(temp)
    return answer

if __name__ == "__main__":
    print(solution(5, [1, 20, 28, 18, 11], [30, 1, 21, 17, 28]))