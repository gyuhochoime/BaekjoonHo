import sys
n = int(sys.stdin.readline())
dp = [0] * (n + 1)
sqrt = [x ** 2 for x in range(1, 225)]
for i in range(1, n + 1):
    mini = []
    for j in sqrt:
        if j > i:
            break
        mini.append(dp[i-j])
    dp[i] = min(mini) + 1
print(dp[-1])
