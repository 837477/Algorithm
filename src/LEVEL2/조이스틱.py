def solution(name):
    A = ord('A')
    Z = ord('Z')
    M = ord('M')
    answer = 0
    cursor = 0
    result = []

    for alpha in list(map(ord, name)):
        result.append(alpha if alpha != A else 0)

    len_name = len(result)
    while True:
        if result[cursor] != 0:
            answer += result[cursor] - A if result[cursor] <= M else Z - result[cursor] + 1
            result[cursor] = 0
        
        if sum(result) == 0:
            break

        l_cnt = r_cnt = 0
        while True:
            l_cnt += 1
            idx = (cursor - l_cnt) % len_name
            if result[idx] != 0:
                break
        while True:
            r_cnt += 1
            idx = (cursor + r_cnt) % len_name
            if result[idx] != 0:
                break
        
        if l_cnt < r_cnt:
            answer += l_cnt
            cursor = cursor - l_cnt if cursor - l_cnt > 0 else len_name - abs(cursor - l_cnt)
        else:
            answer += r_cnt
            cursor = cursor + r_cnt

    return answer


if __name__ == "__main__":
    print(solution("AZAZA"))

# a b c d e f g h i j k l m    n o p q r s t u v w x y z