import sys
from collections import deque
n = int(sys.stdin.readline())
ds = list(map(int, sys.stdin.readline().split()))
queuestack = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
insert = list(map(int, sys.stdin.readline().split()))
queue = deque()
value = []
for i in range(n):
    if ds[i] == 0:
        queue.append(queuestack[i])
if len(queue) == 0:
    print(*insert)
else:
    for i in range(m):
        queue.appendleft(insert[i])
        value.append(queue.pop())
    print(*value)
