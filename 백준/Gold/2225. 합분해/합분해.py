import sys
n, m = map(int, sys.stdin.readline().split())
dp = [[1] * (n + 1) for _ in range(m)]
for i in range(1, m):
    for j in range(1, n + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
print(dp[m-1][n])
