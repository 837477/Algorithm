from collections import defaultdict

def solution(clothes):
    cloth_set = defaultdict(int)
    for cloth in clothes:
        cloth_set[cloth[1]] += 1

    answer = 1
    for value in cloth_set.values():
        answer *= (value + 1)
    return answer - 1

if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "headgear"], ["green_turban", "headgear"]]))

'''
defaultdict(<class 'int'>, {'headgear': 3})
'''