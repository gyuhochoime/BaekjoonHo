import sys
def dfs(a, lst):
    if a == m:
        ans.append(lst)
        return
    prev = -1
    for i in range(n):
        if visited[i] == 0 and arr[i] != prev:
            prev = arr[i]
            visited[i] = 1
            dfs(a + 1, lst + [arr[i]])
            visited[i] = 0
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
visited = [0] * n
dfs(0, [])
for i in ans:
    print(*i)