import sys
import math
T = int(sys.stdin.readline())
sosu = [0] * 1000001
for i in range(2, int(math.sqrt(1000001))):
    if sosu[i] == 0:
        for j in range(i * i, 1000001, i):
            sosu[j] = 1
for _ in range(T):
    a = int(sys.stdin.readline())
    cnt = 0
    for i in range(2, a // 2 + 1):
        if sosu[i] == 0 and sosu[a-i] == 0:
            cnt += 1
    print(cnt)
