import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
cnt += n // 3 + m // 3 + k // 3
an = n % 3
am = m % 3
ak = k % 3
if an == am == ak:
    cnt += an
elif an + am + ak <= 2:
    cnt += 1
else:
    cnt += 2
print(cnt)
