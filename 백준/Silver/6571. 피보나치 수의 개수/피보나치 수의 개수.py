import sys
dp = [0] * 482
dp[1], dp[2] = 1, 2
for i in range(3, 482):
    dp[i] = dp[i-1] + dp[i-2]
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    a = b = 0
    for i in range(1, 482):
        if dp[i] >= n:
            a = i
            break
    for i in range(a, 482):
        if dp[i] > m:
            b = i
            break
    print(b - a)
