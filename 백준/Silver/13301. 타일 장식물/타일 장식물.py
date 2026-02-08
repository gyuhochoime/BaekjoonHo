import sys
n = int(sys.stdin.readline())
if n == 1:
    print(4)
elif n == 2:
    print(6)
else:
    dp = [0] * (n + 1)
    dp[0], dp[1] = 4, 6
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n-1])
