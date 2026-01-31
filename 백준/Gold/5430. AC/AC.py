import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    seq = sys.stdin.readline().strip()
    a = int(sys.stdin.readline())
    b = sys.stdin.readline().strip()
    rev = False
    error = False
    if b == "[]":
        arr = []
    else:
        arr = list(map(int, b[1:-1].split(",")))
    arr = deque(arr)
    for i in seq:
        if i == "R":
            rev = not rev
        elif i == "D":
            if len(arr) == 0:
                error = True
                break
            if rev == False:
                arr.popleft()
            elif rev == True:
                arr.pop()
    if error == True:
        print("error")
    else:
        if rev == True:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")
