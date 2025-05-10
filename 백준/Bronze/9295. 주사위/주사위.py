import sys
T = int(sys.stdin.readline().rstrip())
for i in range(1, T + 1):
    tot = 0
    n, m = map(int, sys.stdin.readline().rstrip().split())
    tot = n + m
    print("Case %d: %d" % (i, tot))
