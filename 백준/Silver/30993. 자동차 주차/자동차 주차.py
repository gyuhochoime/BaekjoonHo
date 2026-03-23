import sys
from math import comb
n, a, b, c = map(int, sys.stdin.readline().split())
tot = 1
tot *= comb(n, a)
n -= a
tot *= comb(n, b)
print(tot)
