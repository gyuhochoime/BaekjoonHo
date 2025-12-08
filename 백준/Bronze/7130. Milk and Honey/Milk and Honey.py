import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = int(sys.stdin.readline().rstrip())
tot = 0
for _ in range(a):
    c, h = map(int, sys.stdin.readline().rstrip().split())
    tot += max(n * c, m * h)
print(tot)
