import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
arr = [i for i in range(1, n + 1)]
arr = deque(arr)
cnt = 1
while len(arr) > 1:
    for i in range(1, (cnt ** 3) % len(arr) + 1):
        arr.append(arr.popleft())
    cnt += 1
    arr.pop()
print(arr[0])
