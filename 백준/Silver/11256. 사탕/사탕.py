import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    arr = []
    tot = 0
    cnt = 0
    n, m = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        arr.append(a * b)
    arr.sort(reverse = True)
    for i in arr:
        if tot < n:
            tot += i
            cnt += 1
    print(cnt)
