import sys
arr_1 = list(sys.stdin.readline().rstrip())
arr_2 = list(sys.stdin.readline().rstrip())
n = len(arr_1)
m = len(arr_2)
lcs = []
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr_1[i-1] == arr_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
i, j = n, m
while i > 0 and j > 0:
    if arr_1[i-1] == arr_2[j-1]:
        lcs.append(arr_1[i-1])
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
lcs.reverse()
print(dp[n][m])
for i in lcs:
    print(i, end = "")