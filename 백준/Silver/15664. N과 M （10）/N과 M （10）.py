import sys
def dfs(a, lst):
    if a == m:
        ans.append(lst)
        return
    prev = -1
    for i in range(n):
        if lst: 
            if lst[-1] <= arr[i] and visited[i] == 0 and prev != arr[i]:
                visited[i] = 1
                prev = arr[i]
                dfs(a + 1, lst + [arr[i]])
                visited[i] = 0
        elif visited[i] == 0 and prev != arr[i]:
            visited[i] = 1
            prev = arr[i]
            dfs(a + 1, lst + [arr[i]])
            visited[i] = 0
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = [0] * n
ans = []
dfs(0, [])
for i in ans:
    print(*i)
