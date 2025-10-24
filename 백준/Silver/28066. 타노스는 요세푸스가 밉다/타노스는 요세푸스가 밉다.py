import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [x for x in range(1, n + 1)]
arr = deque(arr)
while len(arr) > m:
    arr.append(arr.popleft())
    for _ in range(m - 1):
        arr.popleft()
print(arr[0])
