import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
ren = int("1" * n)
rem = int("1" * m)
print(ren + rem)
