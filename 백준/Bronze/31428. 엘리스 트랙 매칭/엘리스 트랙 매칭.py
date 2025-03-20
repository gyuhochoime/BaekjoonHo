import sys

n = int(sys.stdin.readline().rstrip())
m = list(map(str, sys.stdin.readline().rstrip().split()))
k = sys.stdin.readline().rstrip()
cnt = 0

for i in m:
    if i == k:
        cnt += 1
print(cnt)
