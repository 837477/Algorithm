import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub("[^-_.\da-z]+", "", answer)
    answer = re.sub("[\.*]{2,}", ".", answer)
    answer = re.sub("^\.{1,}|\.*$", "", answer)
    
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub("\.*$", "", answer)
    while len(answer) <= 2:
        answer += answer[-1]
    return answer