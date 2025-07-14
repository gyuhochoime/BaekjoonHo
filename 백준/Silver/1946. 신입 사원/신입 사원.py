import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    Q = int(sys.stdin.readline().rstrip())
    arr = []
    for i in range(Q):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        arr.append((n, m))
    arr.sort()
    cnt = 0
    le = Q + 1
    for s, l in arr:
        if l < le:
            cnt += 1
            le = l
    print(cnt)
