import sys
T = int(sys.stdin.readline())
tot = 0
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    tot += n * m
print(tot)
