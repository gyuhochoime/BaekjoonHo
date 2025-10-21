import sys
n = int(sys.stdin.readline().rstrip())
arr = dict()
for i in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if a[0] == 1:
        arr[a[2]] = a[1]
    elif a[0] == 2:
        print(arr[a[1]])
