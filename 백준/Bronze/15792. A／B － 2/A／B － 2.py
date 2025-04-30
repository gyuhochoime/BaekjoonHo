import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
k = n / m
print("%0.16f" % k)
