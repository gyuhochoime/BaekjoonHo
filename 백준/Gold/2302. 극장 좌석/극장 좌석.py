import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cnt = 1
dp = [0] * 41
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 3
for i in range(4, 41):
    dp[i] = dp[i-1] + dp[i-2]
if m > 0:
    vip = [int(sys.stdin.readline()) for _ in range(m)]
    a = vip[0] - 1
    b = n - vip[-1]
    cnt *= dp[a] * dp[b]
    if m > 1:
        for i in range(m - 1):
            cnt *= dp[vip[i+1]-vip[i]-1]
    print(cnt)
else:
    print(cnt * dp[n])
