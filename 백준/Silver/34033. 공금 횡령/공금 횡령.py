import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
price = dict()
cnt = 0
for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    price[a] = int(b)
for _ in range(m):
    c, d = map(str, sys.stdin.readline().rstrip().split())
    if price[c] * 1.05 < int(d):
        cnt += 1
print(cnt)
