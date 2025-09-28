import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    cnt = 0
    n, m = map(int, sys.stdin.readline().rstrip().split())
    cnt += n // m
    a = n % m
    if a != 0:
        cnt += 1
    print(cnt)
