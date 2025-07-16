import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    Q = int(sys.stdin.readline().rstrip())
    cnt = n
    for i in range(Q):
        k, s = map(int, sys.stdin.readline().rstrip().split())
        cnt += k * s
    print(cnt)
