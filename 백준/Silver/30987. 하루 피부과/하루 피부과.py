import sys
n, m = map(int, sys.stdin.readline().split())
a, b, c, d, e = map(int, sys.stdin.readline().split())
two = a // 3
one = (b - d) // 2
sang = c - e
fx = two * m ** 3 + one * m ** 2 + sang * m
gx = two * n ** 3 + one * n ** 2 + sang * n
print(fx - gx)
