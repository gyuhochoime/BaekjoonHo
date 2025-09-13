import sys
while True:
    n, m, k, r = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0 and k == 0 and r == 0:
        break
    print(k - m, r - n)
