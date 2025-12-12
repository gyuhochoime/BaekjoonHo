import sys
import math
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
sosu = [0] * 10001
tot = 0
fsu = 0
for i in range(2, int(math.sqrt(10000)) + 1):
    if sosu[i] == 0:
        for j in range(i * i, 10001, i):
            sosu[j] = 1
for i in range(n, m + 1):
    if i > 1 and sosu[i] == 0:
        tot += i
for i in range(n, m + 1):
    if i > 1 and sosu[i] == 0:
        fsu = i
        break
if tot == 0 and fsu == 0:
    print(-1)
else:
    print(tot)
    print(fsu)
