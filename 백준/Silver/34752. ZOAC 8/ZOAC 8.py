import sys
import math
n = int(sys.stdin.readline().rstrip())
sosu = [0] * 100001
zoac = dict()
for i in range(2, int(math.sqrt(100000)) + 1):
    if sosu[i] == 0:
        for j in range(i * i, 100001, i):
            sosu[j] = 1
prefix = [0] * 100001
for i in range(2, 100001):
    if sosu[i] == 0:
        prefix[i] = prefix[i-1] + 1
    else:
        prefix[i] = prefix[i-1]
for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    cnt = 0
    maxi = max(int(b[:5]), int(b[5:]))
    mini = min(int(b[:5]), int(b[5:]))
    cnt = prefix[maxi] - prefix[mini-1]
    zoac[a] = cnt
pride = [(key, value) for key, value in zoac.items()]
pride.sort(key = lambda x: (-x[1], x[0]))
print(pride[0][0])
pride.sort(key = lambda x: (x[1], x[0]))
print(pride[0][0])
