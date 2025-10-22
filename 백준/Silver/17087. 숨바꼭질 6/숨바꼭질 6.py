import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
gori = []
for i in arr:
    gori.append(abs(i - m))
print(math.gcd(*gori))
