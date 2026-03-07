import sys
import math
n = int(sys.stdin.readline())
if n == 3:
    print(0)
else:
    print(math.comb(n, 4))
