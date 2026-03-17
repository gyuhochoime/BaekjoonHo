import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited = [[-1] * n for _ in range(n)]
    visited[si][sj] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    return visited
n, m = map(int, sys.stdin.readline().split())
arr = []
dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
a, b = map(int, sys.stdin.readline().split())
visited = bfs(a - 1, b - 1)
for _ in range(m):
    c, d = map(int, sys.stdin.readline().split())
    arr.append(visited[c-1][d-1])
print(*arr)
