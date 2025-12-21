import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())
new = int(str(m) + str(n))
sosu = [0] * 10000001
for i in range(2, int(math.sqrt(10000000)) + 1):
    if sosu[i] == 0:
        for j in range(i * i, 10000001, i):
            sosu[j] = 1
if sosu[n] == 0 and sosu[new] == 0:
    print("Yes")
else:
    print("No")
