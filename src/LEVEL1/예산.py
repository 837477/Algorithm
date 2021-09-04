def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return d

if __name__ == "__main__":
    print(solution([1,3,2,5,4], 9))
    