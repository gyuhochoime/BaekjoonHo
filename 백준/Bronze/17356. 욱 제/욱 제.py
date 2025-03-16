import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
k = (m - n) / 400
print(1 / (1 + 10 ** k))

