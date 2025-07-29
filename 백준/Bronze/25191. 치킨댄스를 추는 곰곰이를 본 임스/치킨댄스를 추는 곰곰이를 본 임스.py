import sys
t = int(sys.stdin.readline().rstrip())
n, m = map(int, sys.stdin.readline().rstrip().split())
a = n // 2 + m
print(min(a, t))
