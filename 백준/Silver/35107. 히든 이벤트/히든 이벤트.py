import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
ja = n - m
choi = 1.0000000000
b = 1
for _ in range(k):
    tot = 0
    one = 1
    a = ja / n
    b *= a
    one -= b
    tot += one
    if tot <= 1:
        print("%0.10f" % tot)
    else:
        print("%0.10f" % choi)
    n -= 1
    ja -= 1