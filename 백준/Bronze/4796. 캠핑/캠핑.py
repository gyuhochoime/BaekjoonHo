import sys
i = 1
while True:
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0 and k == 0:
        break
    s = k // m
    namoji = k % m
    if n >= namoji:
        print("Case %d: %d" % (i, s * n + namoji))
    else:
        print("Case %d: %d" % (i, s * n + n))
    i += 1
