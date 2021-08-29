def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1 and board[i-1][j] >= 1 and board[i][j-1] >= 1 and board[i-1][j-1] >= 1:
                board[i][j] += min(board[i-1][j], board[i][j-1], board[i-1][j-1])
    _max = max(map(max, board))
    return _max * _max

if __name__ == "__main__":
    # print(solution([[1, 0, 1, 1, 0, 1, 1],
    #                 [1, 1, 1, 1, 1, 1, 1],
    #                 [1, 1, 1, 1, 1, 1, 1],
    #                 [1, 1, 1, 1, 1, 1, 1],
    #                 [0, 1, 0, 0, 1, 1, 1],
    #                 [1, 1, 1, 0, 0, 0, 1],
    #                 [0, 1, 1, 1, 0, 1, 1]]))
    # print(solution([[0,  1,  1,  1,  1],
    #                 [1,  1,  1,  1,  0],
    #                 [1,  1,  1,  1,  1],
    #                 [1,  1,  1,  1,  1],
    #                 [1,  1,  1,  1,  1]]))
    print(solution([[0,0,1,1],
                    [1,1,1,1]]))
