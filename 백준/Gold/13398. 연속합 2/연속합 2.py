import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [arr[:] for _ in range(2)]
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
print(max(max(dp[0]), max(dp[1])))