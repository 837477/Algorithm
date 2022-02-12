from math import ceil
def solution(n,a,b):
    answer = 1
    a, b = ceil(a/2), ceil(b/2)
    while a != b:
        a, b = ceil(a/2), ceil(b/2)
        answer += 1
    return answer

if __name__ == "__main__":
    print(solution(8, 4, 5))