def converter(c):
    if c == '(': return ')'
    elif c == '[': return ']'
    else: return '}'

def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        stack = []
        flag = False
        for value in s:
            if value in {'(', '[', '{'}:
                stack.append(value)
                flag = True
            else:
                if stack and converter(stack[-1]) == value:
                    stack.pop()
        if not stack and flag:
            answer += 1
        s.append(s.pop(0))

    return answer

if __name__ == "__main__":
    print(solution("[](){}"))