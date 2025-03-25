import sys

n = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(9):
    m = int(sys.stdin.readline().rstrip())
    tot += m
nrd = n - tot
print(nrd)
