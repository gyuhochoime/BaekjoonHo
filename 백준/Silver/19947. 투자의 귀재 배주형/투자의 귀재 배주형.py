import sys
n, m = map(int, sys.stdin.readline().split())
dp = [0] * (m + 1)
dp[0] = n
for i in range(1, m + 1):
    dp[i] = int(dp[i-1] * 1.05)
    if i >= 3:
        dp[i] = max(dp[i], int(dp[i-3] * 1.2))
    if i >= 5:
        dp[i] = max(dp[i], int(dp[i-5] * 1.35))
print(dp[m])
