import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
for i in arr:
    print(i, end = " ")
