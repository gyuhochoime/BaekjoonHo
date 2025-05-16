import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = set(arr)
arr = list(arr)
arr.sort()
for i in arr:
    print(i, end = " ")
