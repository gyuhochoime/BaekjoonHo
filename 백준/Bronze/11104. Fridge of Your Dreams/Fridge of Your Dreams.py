import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    su = 8388608
    tot = 0
    arr = list(map(int, sys.stdin.readline().rstrip()))
    for i in arr:
        if i == 1:
            tot += su
        su //= 2
    print(tot)
