import sys
n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
dp = [100001] * (m + 1)
for i in arr:
    if i <= m:
        dp[i] = 1
for i in range(1, m + 1):
    for j in arr:
        if i - j > 0 and dp[i-j] != 100001:
            dp[i] = min(dp[i], dp[i-j] + 1)
if dp[m] == 100001:
    print(-1)
else:
    print(dp[m])
