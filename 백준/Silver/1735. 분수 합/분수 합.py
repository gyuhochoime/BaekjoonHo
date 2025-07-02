import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())
k, s = map(int, sys.stdin.readline().rstrip().split())
a = math.lcm(m, s)
son = a // m * n + a // s * k
gong = math.gcd(son, a)
print(son // gong, a // gong)
