import sys
def dfs(a, lst):
    if a == m:
        ans.append(lst)
        return
    for i in range(n):
        dfs(a + 1, lst + [arr[i]])
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
dfs(0, [])
for i in ans:
    print(*i)