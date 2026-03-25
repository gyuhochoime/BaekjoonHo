import sys
n, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
dp = [0] * (k + 1)
dp[0] = 1
for i in arr:
    for j in range(i, k + 1):
        dp[j] += dp[j-i]
print(dp[k])
