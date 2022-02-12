def solution(dartResult):
    areas = {'S': 1, 'D': 2, 'T': 3}
    answer = 0
    last_idx = 0
    score_bag = [0, 0]
    for idx, value in enumerate(dartResult):
        score = 0
        if value in areas:
            score = int(dartResult[last_idx:idx]) ** areas[value]
            score_bag.pop(0)
            score_bag.append(score)
            last_idx = idx+1
        
        if value == '*':
            for idx, value in enumerate(score_bag):
                answer -= value
                answer += (value * 2)
                score_bag[idx] = (value * 2)
            last_idx += 1

        elif value == '#':
            answer -= score_bag[1]
            answer += (score_bag[1] * -1)
            score_bag[1] = (score_bag[1] * -1)
            last_idx += 1

        if score != 0:
            answer += score_bag[1]

    return answer

if __name__ == "__main__":
    print(solution("1D2S3T*"))