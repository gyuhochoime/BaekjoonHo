import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = deque(arr)
pend = deque()
cur = 1
while arr or pend:
    if arr and arr[0] == cur:
        arr.popleft()
        cur += 1
    elif pend and pend[-1] == cur:
        pend.pop()
        cur += 1
    elif arr:
        pend.append(arr.popleft())
    else:
        break
if cur == n + 1:
    print("Nice")
else:
    print("Sad")
