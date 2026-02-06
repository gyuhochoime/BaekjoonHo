import sys
n, m = map(int, sys.stdin.readline().split())
shc = []
dp = [x for x in range(m + 1)]
for _ in range(n):
    lt, rt, km = map(int, sys.stdin.readline().split())
    if rt - lt > km and rt <= m:
        shc.append((lt, rt, km))
shc.sort(key = lambda x: (x[0], x[2]))
idx = 0
for i in range(m + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1] + 1)
    while idx < len(shc) and shc[idx][0] == i:
        lt, rt, km = shc[idx]
        dp[rt] = min(dp[rt], dp[lt] + km)
        idx += 1
print(dp[m])
