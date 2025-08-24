import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
if n > m:
    print(m * 2 + 1)
elif n <= m:
    print(n * 2 - 1)
