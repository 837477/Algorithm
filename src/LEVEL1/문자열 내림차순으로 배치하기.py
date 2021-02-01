import re

def solution(s):
    l = re.findall("[A-Z]", s)
    s = re.sub("[A-Z]", "", s)

    return "".join(sorted(s, reverse=True) + sorted(l, reverse=True))

if __name__ == "__main__":
    print(solution("Zbcdefg"))