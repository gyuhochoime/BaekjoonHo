import sys
from collections import deque
def ice_bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
def new_bfs(si, sj):
    tot = 0
    for di, dj in dirs:
        ni, nj = si + di, sj + dj
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
            tot += 1
    if arr[si][sj] - tot > 0:
        new_arr[si][sj] = arr[si][sj] - tot
        new_glacier.append((si, sj))
    else:
        new_arr[si][sj] = 0
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
year = -1
glacier = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            glacier.append((i, j))
while True:
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for si, sj in glacier:
        if visited[si][sj] == 0:
            ice_bfs(si, sj)
            cnt += 1
    year += 1
    if cnt > 1:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    new_arr = [[0] * m for _ in range(n)]
    new_glacier = []
    for si, sj in glacier:
        new_bfs(si, sj)
    arr = new_arr
    glacier = new_glacier
