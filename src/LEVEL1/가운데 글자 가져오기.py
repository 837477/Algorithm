def solution(s):
    len_ = len(s)
    return s[len_//2] if len_ % 2 == 1 else s[len_//2-1:len_//2+1]