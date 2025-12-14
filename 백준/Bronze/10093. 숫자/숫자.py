import sys

n, m = map(int, sys.stdin.readline().split())
a = min(n, m)
b = max(n, m)

if b - a - 1 > 0:
    print(b - a - 1)
    for i in range(a + 1, b):
        print(i, end=" ")
else:
    print(0)