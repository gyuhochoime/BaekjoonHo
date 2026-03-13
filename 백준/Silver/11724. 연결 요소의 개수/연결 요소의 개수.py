import sys
from collections import deque
def bfs(si):
    q = deque()
    q.append(si)
    visited[si] = 1
    while q:
        a = q.popleft()
        for i in adj[a]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(1, n + 1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)
