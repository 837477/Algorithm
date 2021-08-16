def solution(price, money, count):
    total = 0
    for i in range(1, count+1):
        total += price * i
        
    if money >= total:
        return 0
    return total - money

if __name__ == "__main__":
    print(solution(3, 20, 4))