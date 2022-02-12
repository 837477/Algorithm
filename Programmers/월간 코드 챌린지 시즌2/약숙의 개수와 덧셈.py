def yack (num):
    answer = 1
    for i in range(2, num+1):
        if num % i == 0:
            answer += 1
    return answer

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if yack(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer

if __name__ == "__main__":
    print(solution(13, 17))