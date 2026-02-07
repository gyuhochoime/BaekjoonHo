import sys
n = int(sys.stdin.readline())
sol = []
dp = [0] * (n + 1)
for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split()) 
    if i + a - 1 <= n:
        dp[i-1+a] = max(dp[i-1+a], b)
        sol.append((i, a, b))
idx = 0
while idx < len(sol):
    gan = sol[idx][0] + sol[idx][1] - 1
    for day, per, mon in sol:
        if day >= gan + 1:
            dp[day-1+per] = max(dp[day-1+per], dp[gan] + mon)
    idx += 1
print(max(dp))
