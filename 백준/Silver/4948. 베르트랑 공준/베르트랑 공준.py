import sys
import math
arr = [0] * 250001
for i in range(2, int(math.sqrt(250000)) + 1):
    if arr[i] == 0:
        for j in range(i * i, 250001, i):
            arr[j] = 1
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if arr[i] == 0 and i > 1:
            cnt += 1
    print(cnt)
