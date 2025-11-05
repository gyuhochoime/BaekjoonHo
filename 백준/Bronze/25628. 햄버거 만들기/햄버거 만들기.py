import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
bun = n // 2
print(min(bun, m))
