import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
a = [0] * (n + 1)
tot = 0
for i in arr:
    for j in range(i, n + 1, i):
        a[j] = 1
for i in range(n + 1):
    if a[i] == 1:
        tot += i
print(tot)
