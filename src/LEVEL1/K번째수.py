def solution(array, commands):
    result = []
    for cmd in commands:
        temp = array[(cmd[0]-1):(cmd[1])]
        temp = sorted(temp)
        result.append(temp[cmd[2]-1])
    return result