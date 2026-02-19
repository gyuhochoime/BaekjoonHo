import sys
n, m = map(int, sys.stdin.readline().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1
k = int(sys.stdin.readline())
con = [[[] for _ in range(m + 1)] for _ in range(n + 1)]
for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    con[a][b].append([c,d])
    con[c][d].append([a,b])
for i in range(n + 1):
    for j in range(m + 1):
        if i > 0 and [i-1,j] not in con[i][j]:
            dp[i][j] += dp[i-1][j]
        if j > 0 and [i,j-1] not in con[i][j]:
            dp[i][j] += dp[i][j-1]
print(dp[n][m])
