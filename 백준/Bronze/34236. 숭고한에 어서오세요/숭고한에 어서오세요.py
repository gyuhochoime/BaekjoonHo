import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = arr[n-1] - arr[n-2]
print(arr[n-1] + m)
