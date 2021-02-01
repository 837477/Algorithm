def solution(arr):
    min_ = min(arr)
    arr.remove(min_)
    if not arr:
        arr = [-1]
    return arr