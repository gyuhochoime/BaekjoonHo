import sys
import math
n = int(sys.stdin.readline().rstrip())
lt = 1
rt = n
while True:
    mid = (lt + rt) // 2
    if mid ** 2 > n:
        rt = mid - 1
    elif mid ** 2 < n:
        lt = mid + 1
    else:
        print(mid)
        break
