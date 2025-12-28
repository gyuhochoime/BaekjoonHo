import sys
from collections import deque
a = list(map(str, sys.stdin.readline().rstrip()))
a = deque(a)
moum = ["a", "e", "i", "o", "u"]
lena = len(a)
while lena > 0:
    if a[0] in moum:
        a.append(a.popleft())
        a.popleft()
        a.popleft()
        lena -= 3
    else:
        lena -= 1
        a.append(a.popleft())
for i in a:
    print(i, end = "")
