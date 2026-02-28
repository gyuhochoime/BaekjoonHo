import sys
n, m = map(int, sys.stdin.readline().split())
dp = [0] * (m + 1)
dp[1] = dp[2] = 1
if m == 2:
    print(11)
else:
    for i in range(3, m + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10
    a = ""
    for i in range(n, m + 1):
        a += str(dp[i])
    print(a)
