import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0
    while q:
        ci, cj = q.popleft()
        ni, nj = ci, cj + 1
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == "." and visited[ni][nj] == -1:
            q.append((ni, nj))
            visited[ni][nj] = visited[ci][cj] + 1
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == "c":
            bfs(i, j)
for i in visited:
    print(*i)
