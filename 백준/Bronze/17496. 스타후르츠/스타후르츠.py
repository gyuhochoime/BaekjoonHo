import sys
n, t, c, p = map(int, sys.stdin.readline().rstrip().split())
hvt = (n - 1) // t
tot = hvt * c * p
print(tot)
