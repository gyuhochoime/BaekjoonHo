import sys
def dfs(a, arr):
    if a == m:
        ans.append(arr)
        return
    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(a + 1, arr + [i])
            visited[i] = 0
n, m = map(int, sys.stdin.readline().split())
ans = []
visited = [0] * (n + 1)
dfs(0, [])
for i in ans:
    print(*i)
