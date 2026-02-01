import sys
n = int(sys.stdin.readline())
dp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
tot = max(dp[-1])
print(tot)
