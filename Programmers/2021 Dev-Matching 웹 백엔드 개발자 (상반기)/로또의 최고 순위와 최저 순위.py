def solution(lottos, win_nums):
    score = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    match_cnt = len(set(lottos) & set(win_nums))
    return [score[match_cnt + lottos.count(0)], score[match_cnt]]



if __name__ == "__main__":
    print(solution(
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12]

        # [45, 4, 35, 20, 3, 9],
        # [20, 9, 3, 45, 4, 35]

        # [0, 0, 0, 0, 0, 0],
        # [38, 19, 20, 40, 15, 25]
    ))
