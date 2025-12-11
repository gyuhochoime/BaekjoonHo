import sys
n, m, k, r, s = map(int, sys.stdin.readline().rstrip().split())
cho = m
cnt = 0
tot = 0
while cnt < n:
    if k - m < r:
        break
    if cho + r <= k:
        cho += r
        cnt += 1
        tot += 1
    else:
        if cho - s < m:
            cho = m
            tot += 1
        else:
            cho -= s
            tot += 1
if tot == 0:
    print(-1)
else:
    print(tot)
