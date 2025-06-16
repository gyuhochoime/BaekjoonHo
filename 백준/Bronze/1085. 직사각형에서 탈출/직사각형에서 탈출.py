import sys
n, m, k, r = map(int, sys.stdin.readline().rstrip().split())
print(min(n, m, k - n, r - m))
