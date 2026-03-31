import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[1] * n for _ in range(2)]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)
bitonic = []
for i in range(n):
    bitonic.append(dp[0][i] + dp[1][i] - 1)
print(max(bitonic))