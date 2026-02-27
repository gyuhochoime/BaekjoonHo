import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
if n > 0:
    arr = deque(list(map(int, sys.stdin.readline().split())))
    box = 0
    tot = 0
    while arr:
        if tot + arr[0] > m:
            tot = arr[0]
            box += 1
            arr.popleft()
        else:
            tot += arr[0]
            arr.popleft()
    if tot != 0:
        box += 1
    print(box)
else:
    print(0)
