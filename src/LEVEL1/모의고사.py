def solution(answers):
    h1 = [1, 2, 3, 4, 5]
    h2 = [2, 1, 2, 3, 2, 4, 2, 5]
    h3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0] * 3
    
    for idx, value in enumerate(answers):
        if value == h1[idx%5]:
            cnt[0] += 1
        if value == h2[idx%8]:
            cnt[1] += 1
        if value == h3[idx%10]:
            cnt[2] += 1

    max_ = max(cnt)
    return [i+1 for i in range(3) if cnt[i] == max_]