import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(str, sys.stdin.readline().rstrip()))
for i in range(len(arr) - 5, len(arr)):
    print(arr[i], end = "")
