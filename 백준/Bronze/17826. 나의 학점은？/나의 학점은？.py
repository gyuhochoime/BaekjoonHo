import sys
from collections import deque
arr = map(int, sys.stdin.readline().rstrip().split())
arr= deque(arr)
n = int(sys.stdin.readline().rstrip())
cnt = 1
while arr:
    if arr[0] == n:
        break
    arr.popleft()
    cnt += 1
if cnt >= 1 and cnt <= 5:
    print("A+")
elif cnt >= 6 and cnt <= 15:
    print("A0")
elif cnt >= 16 and cnt <= 30:
    print("B+")
elif cnt >= 31 and cnt <= 35:
    print("B0")
elif cnt >= 36 and cnt <= 45:
    print("C+")
elif cnt >= 46 and cnt <= 48:
    print("C0")
else:
    print("F")
