import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
tot = n
arr.sort()
for i in arr:
    if tot < 200:
        cnt += 1
        tot += i
    else:
        break
print(cnt)
