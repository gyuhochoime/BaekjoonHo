import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[1] * n for _ in range(2)]
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        dp[0][i] = dp[0][i-1] + 1
    if arr[i] <= arr[i-1]:
        dp[1][i] = dp[1][i-1] + 1
print(max(max(dp[0]), max(dp[1])))
