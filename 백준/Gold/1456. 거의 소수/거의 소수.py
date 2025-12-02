import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
limit = int(math.sqrt(m)) + 1
sosu = [0] * (limit + 1)
for i in range(2, int(math.sqrt(limit)) + 1):
    if sosu[i] == 0:
        for j in range(i * i, limit, i):
            sosu[j] = 1
for i in range(2, limit):
    if sosu[i] == 0:
        alsu = i * i
        while alsu <= m:
            if alsu >= n:
                cnt += 1
            alsu *= i
print(cnt)
