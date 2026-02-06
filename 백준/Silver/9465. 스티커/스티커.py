import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    stu = list(map(int, sys.stdin.readline().split()))
    std = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = stu[0]
    dp[1][0] = std[0]
    if n > 1:
        dp[0][1] = std[0] + stu[1]
        dp[1][1] = std[1] + stu[0]
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + stu[i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + std[i]
    print(max(dp[0][-1], dp[1][-1]))
