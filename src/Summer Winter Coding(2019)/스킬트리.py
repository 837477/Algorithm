def solution(skill, skill_trees):
    skills = list(skill)
    answer = 0
    for skill_tree in skill_trees:
        temp = {}
        for idx, value in enumerate(skill_tree):
            if value in skills: 
                temp[value] = idx
        temp = sorted(temp, key=lambda x:temp[x])
        if skills[:len(temp)] == temp:
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))