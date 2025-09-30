import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
q = deque()
for _ in range(n):
    a = list(map(str, sys.stdin.readline().rstrip().split()))
    if a[0] == "push":
        q.append(a[1])
    elif a[0] == "pop":
        if q == deque([]):
            print(-1)
        else:
            print(q.popleft())
    elif a[0] == "size":
        print(len(q))
    elif a[0] == "empty":
        if q == deque([]):
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if q == deque([]):
            print(-1)
        else:
            print(q[0])
    elif a[0] == "back":
        if q == deque([]):
            print(-1)
        else:
            print(q[len(q)-1])
