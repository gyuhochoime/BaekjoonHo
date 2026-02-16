import sys
n, m = map(int, sys.stdin.readline().split())
egg = [int(sys.stdin.readline()) for _ in range(m)]
egg.sort()
egg_money = 0
price = 0
for i in range(m):
    sell = min(n, m - i)
    money = egg[i] * sell
    if money > egg_money:
        egg_money = money
        price = egg[i]
print(price, egg_money)
