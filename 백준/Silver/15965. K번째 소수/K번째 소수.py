import sys
import math
n = int(sys.stdin.readline().rstrip())
sosu = [0] * 500001
for i in range(2, int(math.sqrt(500000) + 1)):
    if sosu[i] == 0:
        for j in range(i * i, 500000, i):
            sosu[j] = 1
cnt = 0
for i in range(2, 500001):
    if sosu[i] == 0:
        cnt += 1
    if cnt == n:
        print(i)
        break
