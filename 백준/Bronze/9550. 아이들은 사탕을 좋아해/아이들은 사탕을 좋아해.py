import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    tot = 0
    for j in arr:
        tot += j // m
    print(tot)
