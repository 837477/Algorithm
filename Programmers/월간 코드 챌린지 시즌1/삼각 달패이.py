def solution(n):
    result = [[0 for j in range(i)] for i in range(1, n+1)]
    location = [-1, 0]
    p = "down"
    
    num = 1
    for i in range(n):
        if p == "down":
            for j in range(i, n):
                location[0] += 1
                result[location[0]][location[1]] = num
                num += 1
            p = "right"
            
        elif p == "right":
            for j in range(i, n):
                location[1] += 1
                result[location[0]][location[1]] = num
                num += 1
            p = "up"
            
        else:
            for j in range(i, n):
                location[0] -= 1
                location[1] -= 1
                result[location[0]][location[1]] = num
                num += 1
            p = "down"
    
    answer = []
    for i in result:
        for j in i:
            answer.append(j)

    return answer

if __name__ == "__main__":
    print(solution(5))

'''
1
2 9
3 10 8
4 5  6 7
'''

'''
하강 때,
[1]
[2]
[3]
[4]
우측 방향 진행 때,
[1]
[2]
[3]
[4, 5, 6, 7]
상승 때,

'''