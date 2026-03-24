import sys
from collections import deque
def bfs(si, sj):
    global sheep, wolf
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    sheep_tot = wolf_tot = 0
    if arr[si][sj] == "v":
        wolf_tot += 1
    elif arr[si][sj] == "k":
        sheep_tot += 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != "#" and visited[ni][nj] == 0:
                if arr[ni][nj] == "v":
                    wolf_tot += 1
                elif arr[ni][nj] == "k":
                    sheep_tot += 1
                q.append((ni, nj))
                visited[ni][nj] = 1
    if wolf_tot >= sheep_tot:
        wolf += wolf_tot
    else:
        sheep += sheep_tot
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sheep = wolf = 0
for i in range(n):
    for j in range(m):
        if (arr[i][j] == "v" or arr[i][j] == "k") and visited[i][j] == 0:
            bfs(i, j)
print(sheep, wolf)
