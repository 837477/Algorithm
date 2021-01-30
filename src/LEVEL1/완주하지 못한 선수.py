from collections import defaultdict

def solution(participant, completion):
    temp = defaultdict(int)
    for h in completion:
        temp[h] += 1
    for h in participant:
        if h in temp and temp[h] > 0:
            temp[h] -= 1
        else:
            return h