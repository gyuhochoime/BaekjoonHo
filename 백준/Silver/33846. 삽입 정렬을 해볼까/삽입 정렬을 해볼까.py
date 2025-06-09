import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
exp = arr[:m]
exp.sort()
arr[:m] = exp[:m]
for i in arr:
    print(i, end = " ")
