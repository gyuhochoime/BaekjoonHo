import sys
x, y, p, a, b = map(int, sys.stdin.readline().rstrip().split())
po = p + (y - 1) * b
tot = 0
for _ in range(x):
    tot += po
    po -= a
print(tot)
