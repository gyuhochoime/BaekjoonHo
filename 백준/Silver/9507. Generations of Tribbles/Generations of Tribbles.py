import sys
dp = [0] * 68
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4
for i in range(4, 68):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])
