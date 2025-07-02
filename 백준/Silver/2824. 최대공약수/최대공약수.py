import sys
import math
n = int(sys.stdin.readline().rstrip())
arn = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arm = list(map(int, sys.stdin.readline().rstrip().split()))
den = 1
dem = 1
for i in arn:
    den *= i
for i in arm:
    dem *= i
choi = str(math.gcd(den, dem))
print(choi[-9:])
