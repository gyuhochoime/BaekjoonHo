import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
if n <= m:
    cnt = m - n
else:
    while n != m:
        if n % 2 == 1:
            n += 1
            cnt += 1
        else:
            n = n // 2
            cnt += 1
        if n <= m:
            cnt += m - n
            n = m
print(cnt)
