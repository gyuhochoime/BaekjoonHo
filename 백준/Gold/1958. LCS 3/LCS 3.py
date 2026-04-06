import sys
arr_1 = list(sys.stdin.readline().rstrip())
arr_2 = list(sys.stdin.readline().rstrip())
arr_3 = list(sys.stdin.readline().rstrip())
n, m, k = len(arr_1), len(arr_2), len(arr_3)
dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for s in range(1, k + 1):
            if arr_1[i-1] == arr_2[j-1] == arr_3[s-1]:
                dp[i][j][s] = dp[i-1][j-1][s-1] + 1
            else:
                dp[i][j][s] = max(dp[i-1][j][s], dp[i][j-1][s], dp[i][j][s-1])
print(dp[n][m][k])