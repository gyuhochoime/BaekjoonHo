import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
arr = deque()
for i in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if a[0] == 1:
        arr.appendleft(a[1])
    elif a[0] == 2:
        arr.append(a[1])
    elif a[0] == 3:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif a[0] == 4:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif a[0] == 5:
        print(len(arr))
    elif a[0] == 6:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 7:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif a[0] == 8:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])