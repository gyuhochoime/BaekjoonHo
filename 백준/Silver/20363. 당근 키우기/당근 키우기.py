import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
if n >= m:
    print(n + m + m // 10)
else:
    print(m + n + n // 10)
