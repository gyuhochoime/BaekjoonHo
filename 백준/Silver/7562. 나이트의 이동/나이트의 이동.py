import sys
from collections import deque
def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    while q:
        ci, cj = q.popleft()
        if ci == ei and cj == ej:
            return(visited[ci][cj])
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
T = int(sys.stdin.readline())
dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
for _ in range(T):
    n = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    visited = [[0] * n for _ in range(n)]
    ans = bfs(a, b, c, d)
    print(ans)
