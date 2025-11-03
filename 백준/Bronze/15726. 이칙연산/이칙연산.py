import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
a = int(n * m / k)
b = int(n / m * k)
print(max(a, b))
