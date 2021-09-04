def solution(arr):
    num = max_ = min(arr)
    arr.remove(max_)
    while True:
        flag = True
        for a in arr:
            if num % a != 0:
                flag = False
                break
        if flag:
            return num
        num += max_

if __name__ == "__main__":
    print(solution([2, 6, 8, 14]))