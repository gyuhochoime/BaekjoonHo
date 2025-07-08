import sys
import math
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(math.lcm(n, m))
