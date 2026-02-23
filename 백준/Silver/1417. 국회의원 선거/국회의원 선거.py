import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n - 1)]
arr.sort()
cnt = 0
if n == 1:
    print(0)
else:
    if m <= arr[-1]:
        while m <= arr[-1]:
            m += 1
            cnt += 1
            arr[-1] -= 1
            arr.sort()
        print(cnt)
    else:
        print(0)
