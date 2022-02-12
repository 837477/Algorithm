def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


if __name__ == "__main__":
    solution([2,2,3,3], 10)
