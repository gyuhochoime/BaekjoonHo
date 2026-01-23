import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = deque(arr)
    cnt = 0
    b = m
    done = False
    while arr and not done:
        a = len(arr)
        for _ in range(a):
            ma = max(arr)
            if b == 0 and arr[0] == ma:
                cnt += 1
                arr.popleft()
                done = True
                break
            elif b == 0 and arr[0] != ma:
                b = len(arr) - 1
                arr.append(arr.popleft())
            if arr[0] == ma:
                arr.popleft()
                cnt += 1
                b -= 1
            else:
                arr.append(arr.popleft())
                b -= 1
    print(cnt)
