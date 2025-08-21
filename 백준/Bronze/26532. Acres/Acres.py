import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = (n * m) // 24200
b = (n * m) % 24200
if b == 0:
    print(a)
else:
    print(a + 1)
