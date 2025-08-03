import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    print(sum(arr))
