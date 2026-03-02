import sys
T = int(sys.stdin.readline())
dp = [0] * 10001
dp[1], dp[2] = 1, 1
for i in range(3, 10001):
    dp[i] = dp[i-1] + dp[i-2]
for i in range(1, T + 1):
    n, m = map(int, sys.stdin.readline().split())
    a = dp[n] % m
    print("Case #%d: %d" % (i, a))
