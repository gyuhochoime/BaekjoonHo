import sys
n = int(sys.stdin.readline())
dp = [float(sys.stdin.readline()) for _ in range(n)]
for i in range(1, n):
    dp[i] = max(dp[i-1] * dp[i], dp[i])
print("%.3f" % max(dp))
