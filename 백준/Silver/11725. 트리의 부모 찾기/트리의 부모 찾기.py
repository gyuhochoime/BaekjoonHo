import sys
from collections import deque
def bfs(si):
    q = deque()
    q.append(si)
    visited[si] = 0
    while q:
        ci = q.popleft()
        for tmp in arr[ci]:
            if visited[tmp] == -1:
                q.append(tmp)
                visited[tmp] = ci
n = int(sys.stdin.readline())
arr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [-1] * (n + 1)
bfs(1)
for i in range(2, n + 1):
    print(visited[i])
