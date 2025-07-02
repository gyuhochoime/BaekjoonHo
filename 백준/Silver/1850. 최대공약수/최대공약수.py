import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())
choi = math.gcd(n, m)
print(choi * "1")
