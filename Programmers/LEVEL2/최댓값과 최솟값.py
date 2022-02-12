def solution(s):
    temp = list(map(int, s.split(' ')))
    return str(min(temp)) + " " + str(max(temp))

if __name__ == "__main__":
    print(solution("1 2 3 4"))