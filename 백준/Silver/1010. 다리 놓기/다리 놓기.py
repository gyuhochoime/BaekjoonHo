import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    we = 1
    su = 1
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n > m // 2:
        n = m - n
    for j in range(n):
        we *= m - j
    for j in range(1, n + 1):
        su *= j
    tot = we // su
    print(tot)
