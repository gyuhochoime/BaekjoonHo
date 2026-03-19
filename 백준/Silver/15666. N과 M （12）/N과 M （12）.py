import sys
def dfs(a, lst):
    if a == m:
        ans.append(lst)
        return
    res = -1
    for i in range(n):
        if lst:
            if lst[-1] <= arr[i] and arr[i] != res:
                res = arr[i]
                dfs(a + 1, lst + [arr[i]])
        else:
            if arr[i] != res:
                res = arr[i]
                dfs(a + 1, lst + [arr[i]])
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
dfs(0, [])
for i in ans:
    print(*i)
