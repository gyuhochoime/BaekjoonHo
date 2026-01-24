import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
s = deque()
for _ in range(n):
    arr = list(map(str, sys.stdin.readline().rstrip().split()))
    if arr[0] == "add":
        if int(arr[1]) not in s:
            s.append(int(arr[1]))
    elif arr[0] == "check":
        if int(arr[1]) in s:
            print(1)
        else:
            print(0)
    elif arr[0] == "all":
        s = [x for x in range(1, 21)]
        s = deque(s)
    elif arr[0] == "empty":
        s = deque()
    elif arr[0] == "toggle":
        if int(arr[1]) not in s:
            s.append(int(arr[1]))
        else:
            for _ in range(len(s)):
                if s[0] == int(arr[1]):
                    s.popleft()
                    break
                else:
                    s.append(s.popleft())
    elif arr[0] == "remove":
        if int(arr[1]) in s:
            for _ in range(len(s)):
                if s[0] == int(arr[1]):
                    s.popleft()
                    break
                else:
                    s.append(s.popleft())
