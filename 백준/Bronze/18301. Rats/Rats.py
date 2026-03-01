import sys
n, m, k = map(int, sys.stdin.readline().split())
print(((n + 1) * (m + 1)) // (k + 1) - 1)
