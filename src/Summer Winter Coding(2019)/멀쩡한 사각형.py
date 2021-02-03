def gcd(n1, n2):
    min_ = min(n1, n2)
    while True:
        if n1 % min_ == 0 and n2 % min_ == 0:
            break
        min_ -= 1
    return min_

def solution(w,h):
    return w * h - (w + h - gcd(w, h))