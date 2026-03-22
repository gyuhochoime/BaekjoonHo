import sys
from collections import deque
from itertools import combinations
first = True
while True:
    arr = deque(list(map(int, sys.stdin.readline().split())))
    a = arr.popleft()
    if a == 0:
        break
    if not first:
        print()
    first = False
    lst = list(combinations(arr, 6))
    for i in lst:
        print(*i)
