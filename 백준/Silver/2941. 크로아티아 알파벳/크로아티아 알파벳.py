import sys
from collections import deque
n = list(sys.stdin.readline().rstrip())
n = deque(n)
cnt = 0
while n:
    if len(n) > 1 and n[0] == "c" and n[1] == "=":
        n.popleft()
        n.popleft()
        cnt += 1
    elif len(n) > 1 and n[0] == "c" and n[1] == "-":
        n.popleft()
        n.popleft()
        cnt += 1
    elif len(n) > 2 and n[0] == "d" and n[1] == "z" and n[2] == "=":
        n.popleft()
        n.popleft()
        n.popleft()
        cnt += 1
    elif len(n) > 1 and n[0] == "d" and n[1] == "-":
        n.popleft()
        n.popleft()
        cnt += 1
    elif len(n) > 1 and n[0] == "l" and n[1] == "j":
        n.popleft()
        n.popleft()
        cnt += 1
    elif len(n) > 1 and n[0] == "n" and n[1] == "j":
        n.popleft()
        n.popleft()
        cnt += 1
    elif len(n) > 1 and n[0] == "s" and n[1] == "=":
        n.popleft()
        n.popleft()
        cnt += 1
    elif len(n) > 1 and n[0] == "z" and n[1] == "=":
        n.popleft()
        n.popleft()
        cnt += 1
    else:
        n.popleft()
        cnt += 1
print(cnt)
