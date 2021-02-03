def solution(priorities, location):
    bufer = [(idx, value) for idx, value in enumerate(priorities)]
    rank = 0
    while bufer:
        target = bufer.pop(0)
        if bufer and target[1] < max([i[1] for i in bufer]): # 출력 대상이 기존 것보다 우선순위가 낮은 경우 !
            bufer.append(target)
            continue
        else:
            rank += 1
        if target[0] == location:
            break

    return rank
    

if __name__ == "__main__":
    # print(solution([1, 1, 9, 1, 1, 1], 0))
    print(solution([2, 1, 3, 2], 2))

'''
1! // 1 9 1 1 1
1 // 9 1 1 1 1!
9 // 1 1 1 1! 1
1 // 1 1 1! 1
1 // 1 1! 1
1 // 1! 1       


2 // 1 3 2 cnt = 1, location = 1
1 // 3 2 2 cnt = 2
3 // 2 2 1
2 // 2 1
2 // 1
1 // 
'''
