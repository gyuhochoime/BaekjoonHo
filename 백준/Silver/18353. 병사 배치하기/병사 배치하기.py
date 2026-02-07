import sys
n = int(sys.stdin.readline())
sol = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if sol[i] < sol[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
