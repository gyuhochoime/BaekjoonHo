import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    dp = [0] * n
    if n == 1:
        dp[0] = 1
        print(dp[0])
    elif n == 2:
        dp[1] = 2
        print(dp[1])
    elif n == 3:
        dp[2] = 4
        print(dp[2])
    else:
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[-1])
