import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 1
tot = 0
for i in arr:
    if i != cnt:
        tot += 1
    cnt += 1
print(tot)
