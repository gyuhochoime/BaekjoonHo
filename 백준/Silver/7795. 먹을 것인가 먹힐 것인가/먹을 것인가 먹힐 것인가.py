import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0
    start = 0
    a = sorted(list(map(int, sys.stdin.readline().split())))
    b = sorted(list(map(int, sys.stdin.readline().split())))
    for i in range(n):
        while True:
            if start == m or a[i] <= b[start]:
                cnt += start
                break
            else:
                start += 1
    print(cnt)
