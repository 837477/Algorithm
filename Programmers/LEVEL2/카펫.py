def solution(brown, yellow):
    s = brown + yellow
    for i in range(s, 2, -1):
        if s % i == 0 and yellow == (i-2) * (s//i - 2):
            return [i, s//i]

if __name__ == "__main__":
    print(solution(10, 2))

