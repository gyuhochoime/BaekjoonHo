import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
tot = 0
arr = deque()
for i in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if a[0] == 1:
        arr.appendleft([a[1], a[2]])
        arr[0][1] -= 1
        if arr[0][1] == 0:
            tot += arr[0][0]
            arr.popleft()
    elif a[0] == 0:
        if arr:
            arr[0][1] -= 1
            if arr[0][1] == 0:
                tot += arr[0][0]
                arr.popleft()
print(tot)
