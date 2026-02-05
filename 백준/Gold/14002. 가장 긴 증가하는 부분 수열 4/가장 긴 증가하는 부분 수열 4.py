import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
a = max(dp)
res = []
seq = a
for i in range(n - 1, -1, -1):
    if dp[i] == seq:
        res.append(arr[i])
        seq -= 1
print(a)
print(*res[::-1])
