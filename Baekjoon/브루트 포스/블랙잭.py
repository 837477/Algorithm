n, m = map(int, input().split())
cards = list(map(int, input().split()))


# 1차 일반적인 3중 포문
result = cards[-1]
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if m >= (cards[i] + cards[j] + cards[k]):
                result = max(result, cards[i] + cards[j] + cards[k])
print(result)

# 2차 combinations를 사용한 방법
from itertools import combinations
result = cards[-1]
for card_set in combinations(cards, 3):
    temp = sum(card_set)
    if result < temp <= m:
        result = temp
print(result)
