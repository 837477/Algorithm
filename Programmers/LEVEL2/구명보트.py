def solution(people, limit):
    answer = len(people)
    people.sort()
    s = 0
    e = answer - 1
    while s < e:
        if people[s] + people[e] <= limit:
            s += 1
            answer -= 1
        e -= 1
    return answer

if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100))

