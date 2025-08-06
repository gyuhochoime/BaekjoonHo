import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
print(max(n - m, m) * max(n - k, k) * 4)
