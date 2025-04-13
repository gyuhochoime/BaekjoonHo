import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
a = (n ** 2 / (m ** 2 + k ** 2)) ** (1/2)
h = int(m * a)
w = int(k * a)
print(h, w)
