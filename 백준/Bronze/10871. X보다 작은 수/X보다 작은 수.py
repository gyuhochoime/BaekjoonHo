import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(len(arr)):
    if arr[i] < n:
        print(arr[i], end = " ")
