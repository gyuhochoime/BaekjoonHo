import sys
n = sys.stdin.readline().rstrip()
a = int(sys.stdin.readline())
cnt = 0
for _ in range(a):
    m = sys.stdin.readline().rstrip()
    ring = m + m
    if n in ring:
        cnt += 1
print(cnt)
