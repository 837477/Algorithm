'''
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
    return ' '.join(answer)
'''

def solution(s):
    return ' '.join([''.join([c.upper() if idx % 2 == 0 else c.lower() for idx, c in enumerate(word)]) for word in s.split(' ')])