import sys
import math
from functools import reduce
sosu = []
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
a = [0] * (arr[n-1] + 1)
for i in range(2, int(math.sqrt(arr[n-1]) + 1)):
    if a[i] == 0:
        for j in range(i * i, arr[n-1] + 1, i):
            a[j] = 1
for i in arr:
    if a[i] == 0:
        sosu.append(i)
if sosu:
    print(reduce(math.lcm, sosu))
else:
    print(-1)
