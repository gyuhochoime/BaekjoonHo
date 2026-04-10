import sys
from collections import deque
def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0
    while q:
        ci, cj = q.popleft()
        if ci == ei and cj == ej:
            return visited[ei][ej]
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 8 and 0 <= nj < 8 and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
si, sj = map(int, sys.stdin.readline().split())
ei, ej = map(int, sys.stdin.readline().split())
visited = [[-1] * 8 for _ in range(8)]
dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
print(bfs(si - 1, sj - 1, ei - 1, ej - 1))