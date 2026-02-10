import sys
n = int(sys.stdin.readline())
if n == 1:
    print(1)
elif n == 2:
    print(1)
elif n == 3:
    print(1)
else:
    dp = [0] * n
    dp[0], dp[1], dp[2] = 1, 1, 1
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-3]
    print(dp[n-1])
