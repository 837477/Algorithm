def solution(s):
    len_ = len(s)
    if len_ % 2 == 1:
        return s[len_//2]
    else:
        return s[len_//2-1:len_//2+1]