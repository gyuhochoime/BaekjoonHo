import sys
from collections import deque
def bfs(si, sj):
    global sheep, wolf
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    she = wol = 0
    if arr[si][sj] == "o":
        she = 1
    elif arr[si][sj] == "v":
        wol = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == "." and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                elif arr[ni][nj] == "o" and visited[ni][nj] == 0:
                    she += 1
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                elif arr[ni][nj] == "v" and visited[ni][nj] == 0:
                    wol += 1
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    if she > wol:
        sheep += she
    else:
        wolf += wol
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sheep = wolf = 0
for i in range(n):
    for j in range(m):
        if (arr[i][j] == "v" or arr[i][j] == "o") and visited[i][j] == 0:
            bfs(i, j)
print(sheep, wolf)
