import sys
from collections import deque
arr = deque()
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = list(sys.stdin.readline().rstrip().split())
    if a[0] == "push_front":
        arr.appendleft(a[1])
    elif a[0] == "push_back":
        arr.append(a[1])
    elif a[0] == "pop_front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif a[0] == "pop_back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif a[0] == "size":
        print(len(arr))
    elif a[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif a[0] == "back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
