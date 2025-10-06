import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [i for i in range(1, n + 1)]
arr = deque(arr)
yo = []
while arr:
    for _ in range(m - 1):
        arr.append(arr.popleft())
    yo.append(arr.popleft())
print("<" + ", ".join(map(str, yo)) + ">")
