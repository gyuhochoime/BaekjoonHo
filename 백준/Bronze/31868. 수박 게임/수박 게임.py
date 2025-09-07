import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = 2 ** (n - 1)
print(m // a)
