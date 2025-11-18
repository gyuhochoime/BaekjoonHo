import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    print(min(arr), max(arr))
