import itertools

def solution(numbers):
    list_number = list(numbers)
    n = int(''.join(sorted(list_number, reverse=True)))
    a = set(list(range(3, n + 1, 2)))
    for i in range(3, n + 1, 2):
        if i in a:
            a -= set(range(i*2, n + 1, i))
    a.add(2)

    case = []
    for i in range(len(list_number), 0, -1):
        case += list(map(''.join, itertools.permutations(list(numbers), i)))
    
    case = set(map(int, case))
    answer = 0
    for c in case:
        if c in a:
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution("71"))


'''
{'1', '0'}
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
'''