import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse = True)
tot = 0
for i in range(n, 0, -1):
    tot += 2 ** (i - 1) * arr[n-i]
print(tot % 1000000007)
