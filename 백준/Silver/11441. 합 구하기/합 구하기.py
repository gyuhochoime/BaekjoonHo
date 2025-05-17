import sys
k = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(sum(arr[n-1:m]))
