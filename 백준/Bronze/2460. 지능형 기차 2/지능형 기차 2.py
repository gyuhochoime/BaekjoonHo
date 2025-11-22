import sys
tot = 0
maxi = 0
for _ in range(10):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    tot -= s
    tot += e
    maxi = max(tot, maxi)
print(maxi)
