import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
tmp = m
for i in arr:
    if i <= tmp:
        tmp += 1
print(tmp)
