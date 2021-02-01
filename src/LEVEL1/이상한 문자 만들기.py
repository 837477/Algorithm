def solution(s):
    answer = []
    for word in s.split():
        temp = ""
        for idx, c in enumerate(word):
            if idx % 2 == 0:
                temp += c.upper()
            else:
                temp += c.lower()
        answer.append(temp)
    return " ".join(answer)