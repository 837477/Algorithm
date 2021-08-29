def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    return answer

if __name__ == "__main__":
    print(solution([1, 4, 2], [5, 4, 4]))