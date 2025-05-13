import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr.append([n, m])
arr.sort()
for i in range(len(arr)):
    print(arr[i][0], arr[i][1], end = "\n")
