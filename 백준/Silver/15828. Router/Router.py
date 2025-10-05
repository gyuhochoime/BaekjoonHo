import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
arr = deque()
while True:
    a = int(sys.stdin.readline().rstrip())
    if a == -1:
        break
    if a == 0:
        arr.popleft()
    else:
        if len(arr) < n:
            arr.append(a)
if len(arr) == 0:
    print("empty")
else:
    for i in arr:
        print(i, end = " ")
