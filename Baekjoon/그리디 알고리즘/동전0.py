n, money = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins.sort(reverse=True)

result = 0
for coin in coins:
    result += money // coin
    money %= coin

print(result)