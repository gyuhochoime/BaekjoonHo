import sys
n, m, k, r = map(int, sys.stdin.readline().rstrip().split())
print(abs((n + r) - (m + k)))
