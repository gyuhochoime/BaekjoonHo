import sys
n, m = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(1, n + 1):
    a = str(i)
    for j in a:
        if j == str(m):
            cnt += 1
print(cnt)
