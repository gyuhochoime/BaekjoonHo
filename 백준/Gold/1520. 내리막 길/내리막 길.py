import sys
sys.setrecursionlimit(10 ** 9)
def dfs(ci, cj):
    if dp[ci][cj] == -1:
        dp[ci][cj] = 0
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] > arr[ci][cj]: # 내리막 길인 경우
                dp[ci][cj] += dfs(ni, nj)
    return dp[ci][cj]
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dp[0][0] = 1
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
print(dfs(n - 1, m - 1))
