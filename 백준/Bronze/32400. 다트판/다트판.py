import sys
from collections import deque
bob = 10.5
alice = 0
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = deque(arr)
while True:
    if arr[0] == 20:
        alice = (arr[0] + arr[1] + arr[19]) / 3
        break
    arr.append(arr.popleft())
if bob > alice:
    print("Bob")
elif bob == alice:
    print("Tie")
else:
    print("Alice")
