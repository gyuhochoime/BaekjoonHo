import sys
n = int(sys.stdin.readline())
if n == 1:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i-2] + dp[i//2]) % 1000000000
    print(dp[n])
