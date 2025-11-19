import sys
tot = 0
full = 0
for _ in range(4):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    tot -= n
    tot += m
    full = max(full, tot)
print(full)
