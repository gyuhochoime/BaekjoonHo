import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = int(sys.stdin.readline().rstrip())
tot = n + m
if tot >= a * 2:
    print(tot - a * 2)
else:
    print(tot)
