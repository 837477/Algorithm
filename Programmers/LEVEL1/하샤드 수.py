def solution(x):
    a = list(map(int, list(str(x))))
    return True if x % sum(a) == 0 else False
