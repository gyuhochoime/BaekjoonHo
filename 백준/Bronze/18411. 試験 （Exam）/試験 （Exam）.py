import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse = True)
print(arr[0] + arr[1])
