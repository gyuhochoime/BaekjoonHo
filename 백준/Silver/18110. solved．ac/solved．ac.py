import sys
import math
from collections import deque
n = int(sys.stdin.readline().rstrip())
arr = []
jul = math.floor((n / 100) * 15 + 0.5)
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    arr.append(a)
arr.sort()
arr = deque(arr)
if jul > 0:
    for _ in range(jul):
        arr.pop()
        arr.popleft()
if n == 0:
    print(0)
else:
    print(math.floor(sum(arr) / len(arr) + 0.5))
