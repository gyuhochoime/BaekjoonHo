import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(m):
    k, r, s = list(map(str, sys.stdin.readline().rstrip().split()))
    arr.append([int(k), int(r), s])
arr.sort()
arr.sort(key = lambda x: x[1])
for i in range(m):
    print(arr[i][2], end = "")
