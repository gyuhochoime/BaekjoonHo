import sys
s, d, i, l, n = map(int, sys.stdin.readline().rstrip().split())
m = s + d + i + l
if m < n * 4:
    print(n * 4 - m)
else:
    print(0)
