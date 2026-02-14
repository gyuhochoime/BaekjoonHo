import sys
import math
n, m = map(int, sys.stdin.readline().split())
if n == m:
    print(1)
else:
    print(math.comb(n - 1, m - 1))
