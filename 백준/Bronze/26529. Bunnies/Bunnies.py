import sys
dp = [0] * 46
dp[0], dp[1] = 1, 1
for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])
