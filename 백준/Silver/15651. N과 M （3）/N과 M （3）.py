import sys
def dfs(a, arr):
    if a == m:
        ans.append(arr)
        return
    for i in range(1, n + 1):
        dfs(a + 1, arr + [i])
n, m = map(int, sys.stdin.readline().split())
ans = []
dfs(0, [])
for i in ans:
    print(*i)
