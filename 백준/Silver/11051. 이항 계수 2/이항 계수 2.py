import sys
n, m = map(int, sys.stdin.readline().split())
tot = 1
for i in range(n, n - m, -1):
    tot *= i
for i in range(m, 1, -1):
    tot //= i
print(tot % 10007)
