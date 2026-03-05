import sys
from collections import deque
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
def bfs(si, sj):
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
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    print(cnt)
