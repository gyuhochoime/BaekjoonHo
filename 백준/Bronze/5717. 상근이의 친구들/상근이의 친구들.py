import sys
while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0:
        break
    print(n + m)
