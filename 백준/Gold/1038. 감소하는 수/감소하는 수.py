import sys
from itertools import combinations
n = int(sys.stdin.readline())
arr = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        a = "".join(list(map(str, reversed(list(j)))))
        arr.append(int(a))
arr.sort()
if n >= len(arr):
    print(-1)
else:
    print(arr[n])
