def solution(board, moves):
    # 90도 회전 새로운 상자 만들기
    new_board = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board)-1, -1, -1):
            if board[j][i] != 0:
                temp.append(board[j][i])
        new_board.append(temp)

    answer = 0
    basket = []
    for m in moves:
        m = m - 1

        # 빈 상자 스킵
        if not new_board[m]:
            continue
        
        pick = new_board[m].pop()

        if len(basket) >= 1 and basket[-1] == pick:
            answer += 2
            basket.pop()
            continue
        basket.append(pick)

    return answer

if __name__ == "__main__":
    board = [[0,0,0,0,0],
             [0,0,1,0,3],
             [0,2,5,0,1],
             [4,2,4,4,2],
             [3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))

'''
34
522
1451
34
1213
'''
