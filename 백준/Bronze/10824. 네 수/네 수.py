import sys
a, b, c, d = map(str, sys.stdin.readline().rstrip().split())
n = int(a + b)
m = int(c + d)
print(n + m)
