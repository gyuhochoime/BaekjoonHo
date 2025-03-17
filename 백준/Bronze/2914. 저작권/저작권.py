import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
k = (n * (m - 1)) + 1
print(k)
