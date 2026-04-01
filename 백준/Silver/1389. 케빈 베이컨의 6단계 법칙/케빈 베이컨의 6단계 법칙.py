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
                visited[tmp] = visited[ci] + 1
n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n + 1)]
lst = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1, n + 1):
    visited = [-1] * (n + 1)
    visited[0] = 0
    bfs(i)
    lst.append(sum(visited))
print(lst.index(min(lst)) + 1)