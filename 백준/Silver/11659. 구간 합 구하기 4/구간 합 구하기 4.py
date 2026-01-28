import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
prefix = [0] * (n + 1)
tot = 0
for i in range(n):
    tot += arr[i]
    prefix[i] = tot
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(prefix[b-1] - prefix[a-2])
