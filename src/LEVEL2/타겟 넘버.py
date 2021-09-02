answer = 0
def DFS(numbers, idx, total, target):
    global answer
    if idx == len(numbers) and total == target:
        answer += 1
    if idx == len(numbers):
        return
    DFS(numbers, idx + 1, total + numbers[idx], target)
    DFS(numbers, idx + 1, total - numbers[idx], target)

def solution(numbers, target):
    global answer
    DFS(numbers, 0, 0, target)
    return answer

if __name__ == "__main__":
    print([1, 1, 1])
    print(solution([1, 1, 1], 1))
    # print(solution([1, 1, 1, 1, 1], 3))
    # print(solution([1, 2, 1, 2], 6))
    # print(solution([1, 2, 2, 3, 4, 5, 7, 1], 3))
    
'''
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
'''