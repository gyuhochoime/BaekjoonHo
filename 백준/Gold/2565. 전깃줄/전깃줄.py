import sys
n = int(sys.stdin.readline())
pole = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pole.sort()
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if pole[i][1] > pole[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))