import sys
from collections import deque
def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0
    while q:
        ci, cj = q.popleft()
        if ci == ei and cj == ej:
            return visited[ci][cj]
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 8 and 0 <= nj < 8 and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
si, sj = map(str, sys.stdin.readline().rstrip())
ei, ej = map(str, sys.stdin.readline().rstrip())
si = ord(si) - 97
sj = int(sj) - 1
ei = ord(ei) - 97
ej = int(ej) - 1
visited = [[-1] * 8 for _ in range(8)]
dirs = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
print(bfs(si, sj, ei, ej))