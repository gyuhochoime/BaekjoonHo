import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
cnt = 0
for i in arr:
    if i == n:
        cnt += 1
print(cnt)
