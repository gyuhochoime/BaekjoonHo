import sys
from collections import deque
def bfs(si, sj, ei, ej):
    if si == ei and sj == ej:
        return "Yes"
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                if ni == ei and nj == ej:
                    return "Yes"
    return "No"
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dirs = [(0, 1), (1, 0)]
ans = bfs(0, 0, m - 1, n - 1)
print(ans)
