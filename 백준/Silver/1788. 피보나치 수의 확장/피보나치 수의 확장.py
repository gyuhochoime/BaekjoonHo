import sys
n = int(sys.stdin.readline())
if n > 0:
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000000
    print(1)
    print(abs(dp[n]))
elif n == 0:
    print(0)
    print(0)
elif n < 0:
    a, b = 0, 1
    for i in range(abs(n) - 1):
        a, b = b, (a + b) % 1000000000
    if abs(n) % 2 != 0:
        print(1)
    elif b == 0:
        print(0)
    elif abs(n) % 2 == 0:
        print(-1)
    print(b)
