import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(1, 1001):
    arr.extend([i] * i)
hap = arr[n-1:m]
tot = sum(hap)
print(tot)
