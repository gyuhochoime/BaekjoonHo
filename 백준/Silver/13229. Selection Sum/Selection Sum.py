import sys
a = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    tot = sum(arr[n:m+1])
    print(tot)
