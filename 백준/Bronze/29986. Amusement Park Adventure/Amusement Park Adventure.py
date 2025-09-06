import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
arr.sort()
for i in arr:
    if i <= m:
        cnt += 1
print(cnt)
