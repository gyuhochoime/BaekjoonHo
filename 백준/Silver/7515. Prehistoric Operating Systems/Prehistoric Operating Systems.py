import sys
dp = [0] * 41
dp[1], dp[2] = 2, 3
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]
n = int(sys.stdin.readline())
for i in range(1, n + 1):
    a = int(sys.stdin.readline())
    print("Scenario %d:" % i)
    print(dp[a])
    if i != n:
        print()
