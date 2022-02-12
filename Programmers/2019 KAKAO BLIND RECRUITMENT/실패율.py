from collections import defaultdict
def solution(N, stages):
    cnt = defaultdict(int)
    
    for stage in stages:
        cnt[stage] += 1

    answer = []
    len_stages = len(stages)
    for i in range(1, N + 1):
        if len_stages <= 0:
            answer.append((i, 0))
        else:
            answer.append((i, cnt[i]/len_stages))
        len_stages -= cnt[i]
    
    return [i[0] for i in sorted(answer, key = lambda x: x[1], reverse=True)]
            

if __name__ == "__main__":
    print(solution(3, [1, 2]))