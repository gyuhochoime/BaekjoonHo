import sys
n = int(sys.stdin.readline())
dp = [0] * (n + 10)
dp[0], dp[1], dp[2], dp[3] = 0, 1, 0, 1
for i in range(4, n):
    if dp[i-4] == 0 or dp[i-3] == 0 or dp[i-1] == 0:
        dp[i] = 1
    else:
        dp[i] = 0
if dp[n-1] == 1:
    print("SK")
else:
    print("CY")
