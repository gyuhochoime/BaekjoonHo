import sys
from collections import deque
n = int(sys.stdin.readline())
arr = []
dung = []
rank = []
for _ in range(n):
    hw, wg = map(int, sys.stdin.readline().rstrip().split())
    arr.append((hw, wg))
arr = deque(arr)
for _ in range(n):
    cnt = 0
    for j in range(1, n):
        if arr[0][0] < arr[j][0] and arr[0][1] < arr[j][1]:
            cnt += 1
    dung.append(cnt + 1)
    arr.append(arr.popleft())
print(*dung)
