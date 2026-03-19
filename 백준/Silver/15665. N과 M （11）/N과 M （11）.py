import sys
def dfs(a, lst):
    if len(lst) == m:
        ans.append(lst)
        return
    prev = -1
    for i in range(n):
        if prev != arr[i]:
            prev = arr[i]
            dfs(a + 1, lst + [arr[i]])
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
dfs(0, [])
for i in ans:
    print(*i)
