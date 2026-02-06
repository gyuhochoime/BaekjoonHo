import sys
n, m = map(int, sys.stdin.readline().split())
dp = [[0] * n for _ in range(2)]
dp[0][2] = dp[1][2] = 1
if n > 3:
    dp[0][3], dp[1][3] = 1, 2
    for i in range(4, n):
        dp[0][i] = dp[0][i-1] + dp[0][i-2]
        dp[1][i] = dp[1][i-1] + dp[1][i-2]
fd = sd = 0
while True:
    m -= dp[0][n-1]
    fd += 1
    if m % dp[1][n-1] == 0:
        sd += m // dp[1][n-1]
        break
print(fd)
print(sd)
