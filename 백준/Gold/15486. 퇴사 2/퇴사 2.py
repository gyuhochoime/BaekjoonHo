import sys
n = int(sys.stdin.readline())
sol = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n):
    t, p = sol[i]
    if i > 0:
        dp[i] = max(dp[i], dp[i-1])
    if i + t <= n:
        dp[i+t] = max(dp[i+t], dp[i] + p)
print(max(dp))
