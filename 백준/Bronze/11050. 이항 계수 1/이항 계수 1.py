import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
tot = 1
if m > n // 2:
    for i in range(n - m):
        tot *= n - i
        tot //= i + 1
else:
    for i in range(m):
        tot *= n - i
        tot //= i + 1
print(tot)
