import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
for i in arr:
    if i > 0:
        cnt += 1
print(cnt)
