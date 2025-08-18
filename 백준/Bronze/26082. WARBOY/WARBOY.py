import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
print(int(m // n * k * 3))
