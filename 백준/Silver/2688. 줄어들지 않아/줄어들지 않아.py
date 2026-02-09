import sys
T = int(sys.stdin.readline())
dp = [[1] * 10 for _ in range(64)]
for i in range(1, 64):
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n-1]))
