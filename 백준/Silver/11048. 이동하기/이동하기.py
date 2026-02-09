import sys
n, m = map(int, sys.stdin.readline().split())
candy = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = candy[0][0]
for i in range(n):
    for j in range(m):
        if j == m - 1 and i != n - 1:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + candy[i+1][j])
        elif j != m - 1 and i == n - 1:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + candy[i][j+1])
        elif j != m - 1 and i != n - 1:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + candy[i+1][j])
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + candy[i][j+1])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + candy[i+1][j+1])
print(dp[n-1][m-1])
