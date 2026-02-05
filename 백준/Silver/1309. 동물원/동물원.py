import sys
n = int(sys.stdin.readline())
dp = [0] * n
if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    dp[0], dp[1] = 3, 7
    for i in range(2, n):
        dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901
    print(dp[n-1])
