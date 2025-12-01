import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n + m == 1:
        print(2)
    else:
        print(1)
