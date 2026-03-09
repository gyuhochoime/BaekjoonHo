import sys
from collections import deque
def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
            if ni == ei and nj == ej:
                return visited[ni][nj]
    if visited[ei][ej] == -1:
        return -1
n = int(sys.stdin.readline())
ai, aj, bi, bj = map(int, sys.stdin.readline().split())
visited = [[-1] * n for _ in range(n)]
dirs = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
ans = bfs(ai, aj, bi, bj)
print(ans)
