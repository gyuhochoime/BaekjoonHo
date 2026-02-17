import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
arr = deque([x for x in range(1, n + 1)])
order = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in order:
    while True:
        if arr[0] == i:
            arr.popleft()
            break
        else:
            if arr.index(i) < len(arr) / 2:
                while arr[0] != i:
                    arr.append(arr.popleft())
                    cnt += 1
            else:
                while arr[0] != i:
                    arr.appendleft(arr.pop())
                    cnt += 1
print(cnt)
