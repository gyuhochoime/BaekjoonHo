import sys
from collections import deque
def bfs(si, sj, ei, ej):
    q = deque()
    visited = [[0] * m for _ in range(n)]
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return visited[ei][ej]
        for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
ans = bfs(0, 0, n - 1, m - 1)
print(ans)
