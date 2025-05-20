import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
if n * m > k:
    print(n * m - k)
else:
    print(0)
