import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = list(map(str, sys.stdin.readline().rstrip().split()))
    a = deque(a)
    for _ in range(2):
        a.append(a.popleft())
    for i in a:
        print(i, end = " ")
    print()
