import sys
dp = [0] * 10001
dp[0] = 1
for i in [1, 2, 3]:
    for j in range(i, 10001):
        dp[j] += dp[j-i]
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])
