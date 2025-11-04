import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
bangmu = n / 100 * m
damage = n - bangmu
if damage >= 100:
    print(0)
else:
    print(1)
