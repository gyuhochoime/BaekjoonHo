import sys
n, m = map(int, sys.stdin.readline().split())
bp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    weight = bp[i-1][0]
    value = bp[i-1][1]
    for j in range(1, m + 1):
        if j >= weight:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][m])
