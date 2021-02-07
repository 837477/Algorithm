bag = [0] * 100001

def solution(n):
    for i in range(n+1):
        if i == 0:
            bag[i] = 0
        elif i == 1:
            bag[i] = 1
        else:
            bag[i] = bag[i-1] + bag[i-2]

    return bag[n] % 1234567

if __name__ == "__main__":
    print(solution(5))

# 재귀 깊이 제한 걸려있음...