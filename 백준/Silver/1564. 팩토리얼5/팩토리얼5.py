import sys
n = int(sys.stdin.readline())
tot = 1
tmp = 10 ** 13
for i in range(1, n + 1):
    tot *= i
    while tot % 10 == 0:
        tot //= 10
    tot %= tmp
print(str(tot)[-5:])