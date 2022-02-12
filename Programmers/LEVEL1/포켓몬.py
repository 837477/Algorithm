def solution(nums):
    limit_len = len(nums) // 2
    target_len = len(list(set(nums)))
    return limit_len if target_len >= limit_len else target_len

if __name__ == "__main__":
    print(solution([3, 1, 2, 3]))