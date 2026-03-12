import sys
from itertools import combinations
from collections import deque
def bfs(fi, fj, si, sj, ti, tj):
    q = deque()
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    visited[fi][fj] = visited[si][sj] = visited[ti][tj] = 1
    for xi, xj in virus:
        q.append((xi, xj))
        visited[xi][xj] = 1
        cnt += 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return n * m - cnt - wall
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
safezone = []
wall = 3
virus = []
tot = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            safezone.append((i, j))
        elif arr[i][j] == 1:
            wall += 1
        elif arr[i][j] == 2:
            virus.append((i, j))
a = list(combinations(safezone, 3))
for i in a:
    ai, aj, bi, bj, ci, cj = i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1]
    ans = bfs(ai, aj, bi, bj, ci, cj)
    tot = max(tot, ans)
print(tot)
