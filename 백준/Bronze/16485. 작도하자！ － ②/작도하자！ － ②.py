import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
if n % m == 0:
    print(n // m)
else:
    print(n / m)
