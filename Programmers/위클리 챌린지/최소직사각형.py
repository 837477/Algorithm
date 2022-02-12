def solution(sizes):
    return max(map(max, sizes)) * max(map(min, sizes))


if __name__ == "__main__":
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
