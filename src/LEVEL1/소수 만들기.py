def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def solution(nums):
    answer = 0
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(i+1, nums_len):
            for k in range(j+1, nums_len):
                temp = nums[i] + nums[j] + nums[k]
                if primality(temp):
                    answer += 1
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 7, 6, 4]))