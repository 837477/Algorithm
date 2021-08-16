def grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 50: return 'D'
    else: return 'F'

def solution(scores):
    st_num = len(scores)
    result = []
    
    for i in range(st_num):
        temp = []
        for j in range(st_num):
            temp.append(scores[j][i])
        
        min_ = min(temp)
        max_ = max(temp)
        if scores[i][i] == max_ and temp.count(max_) == 1:
            result.append((sum(temp) - scores[i][i]) / (st_num - 1))
        elif scores[i][i] == min_ and temp.count(min_) == 1:
            result.append((sum(temp) - scores[i][i]) / (st_num - 1))
        else:
            result.append(sum(temp) / st_num)

    return ''.join(list(map(grade, result)))
    
if __name__ == "__main__":
    print(solution([[100,90,98,88,65],
                    [50,45,99,85,77],
                    [47,88,95,80,67],
                    [61,57,100,80,65],
                    [24,90,94,75,65]]))