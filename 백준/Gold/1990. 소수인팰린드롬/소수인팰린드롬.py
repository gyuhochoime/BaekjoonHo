import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())
pel = []
sosu = bytearray(m + 1)
for i in range(2, int(math.sqrt(m)) + 1):
    if sosu[i] == 0:
        for j in range(i * i, m + 1, i):
            sosu[j] = 1
for i in range(n, m + 1):
    if sosu[i] == 0 and str(i) == str(i)[::-1]:
        pel.append(i)
pel.append(-1)
for i in pel:
    print(i)
