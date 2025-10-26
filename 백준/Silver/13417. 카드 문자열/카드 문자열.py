import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(str, sys.stdin.readline().rstrip().split()))
    arr = deque()
    for i in a:
        if len(arr) == 0:
            arr.append(i)
        else:
            if ord(arr[0]) >= ord(i):
                arr.appendleft(i)
            else:
                arr.append(i)
    for i in arr:
        print(i, end = "")
    print()
