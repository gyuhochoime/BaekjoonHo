import sys
import math
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [0] * (n + 1)
cnt = 0
for i in range(2, n + 1):
    if arr[i] == 0:
        for j in range(i, n + 1, i):
            if arr[j] != 1:
                arr[j] = 1
                cnt += 1
                if cnt == m:
                    print(j)
                    break

