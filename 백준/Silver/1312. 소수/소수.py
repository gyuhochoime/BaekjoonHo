import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
for i in range(k):
    n = (n % m) * 10
    a = n // m
print(a)
