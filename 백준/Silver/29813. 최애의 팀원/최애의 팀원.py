import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    arr.append((a, int(b)))
arr = deque(arr)
while len(arr) > 1:
    fass = arr[0][1]
    arr.popleft()
    for _ in range(fass - 1):
        arr.append(arr.popleft())
    arr.popleft()
print(arr[0][0])
