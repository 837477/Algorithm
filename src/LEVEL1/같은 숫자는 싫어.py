def solution(arr):
    answer = []
    for num in arr:
        if answer and answer[-1] == num:
            continue
        answer.append(num)
    return answer

if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1]))