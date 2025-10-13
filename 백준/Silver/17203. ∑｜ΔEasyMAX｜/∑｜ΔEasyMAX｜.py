import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    tot = 0
    c = b - a
    if c == 0:
        print(0)
    else:
        for i in range(c):
            tot += abs(arr[a+i-1] - arr[a+i])
        print(tot)
