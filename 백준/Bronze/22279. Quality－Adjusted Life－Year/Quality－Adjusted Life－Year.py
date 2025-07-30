import sys
T = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(T):
    n, m = map(float, sys.stdin.readline().rstrip().split())
    tot += n * m
print('%.3f' % tot)
