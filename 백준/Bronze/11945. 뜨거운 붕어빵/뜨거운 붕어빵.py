import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
for i in range(n):
    exe = list(map(int, sys.stdin.readline().rstrip()))
    arr = []
    for j in exe[::-1]:
        arr.append(j)
    for k in range(len(arr)):
        print(arr[k], end = "")
    print()
