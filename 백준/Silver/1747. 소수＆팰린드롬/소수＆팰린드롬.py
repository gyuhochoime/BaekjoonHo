import sys
import math
n = int(sys.stdin.readline().rstrip())
a = [0] * 1100001
pel = []
for i in range(2, int(math.sqrt(1100000)) + 1):
    if a[i] == 0:
        for j in range(i * i, 1100001, i):
            a[j] = 1
for i in range(2, 1100001):
    if a[i] == 0 and str(i) == str(i)[::-1]:
        pel.append(i)
for i in pel:
    if i >= n:
        print(i)
        break
