import sys
n = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            continue
        jump = game[i][j]
        if 0 <= i + jump < n:
            dp[i+jump][j] += dp[i][j]
        if 0 <= j + jump < n:
            dp[i][j+jump] += dp[i][j]
print(dp[n-1][n-1])
