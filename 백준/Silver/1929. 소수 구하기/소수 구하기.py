import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())
sosu = [0] * (m + 1)
for i in range(2, int(math.sqrt(m)) + 1):
    if sosu[i] == 0:
        for j in range(i * i, m + 1, i):
            sosu[j] = 1
for i in range(n, m + 1):
    if i > 1 and sosu[i] == 0:
        print(i)
