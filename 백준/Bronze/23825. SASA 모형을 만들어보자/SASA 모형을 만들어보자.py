import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = m // 2
b = n // 2
print(min(b, a))
