import sys
import math
n = int(sys.stdin.readline().rstrip())
garosu = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
gcdf = []
for i in range(n - 1):
    gcdf.append(garosu[i+1] - garosu[i])
degree = math.gcd(*gcdf)
tot = (garosu[-1] - garosu[0]) // degree + 1 - n
print(tot)
