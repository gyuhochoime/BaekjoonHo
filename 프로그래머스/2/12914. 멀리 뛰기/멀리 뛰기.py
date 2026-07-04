def solution(n):
    dp = [1, 2]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(2, n):
            dp.append((dp[i-2] + dp[i-1]) % 1234567)
        return(dp[-1])