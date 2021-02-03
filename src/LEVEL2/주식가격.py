def solution(prices):
    answer = []
    prices_len = len(prices)
    for i in range(prices_len):
        tick = 0
        for j in range(i+1, prices_len):
            tick += 1
            if prices[i] > prices[j]:
                break
        answer.append(tick)
    return answer

'''
# 효율성 탈락 코드
# 로직은 완벽히 똑같은데, 파이썬 구문 처리과정에서 시간차이가 발생
def solution(prices):
    answer = []
    for idx, value in enumerate(prices):
        tick = 0
        for value2 in prices[idx+1:]
            tick += 1
            if value > value2:
                break
        answer.append(tick)
    return answer
'''