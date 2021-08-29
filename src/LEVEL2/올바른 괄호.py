def solution(s):
    stack = 0
    for c in s:
        if c == '(':
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                return False

    return False if stack else True

if __name__ == "__main__":
    print(solution(")()("))