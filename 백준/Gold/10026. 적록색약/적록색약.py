import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] == arr[si][sj]:
                q.append((ni, nj))
                visited[ni][nj] = 1
def colorless_bfs(si, sj):
    q = deque()
    q.append((si, sj))
    colorless_visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if arr[si][sj] == "B":
                if 0 <= ni < n and 0 <= nj < n and colorless_visited[ni][nj] == 0 and arr[ni][nj] == arr[si][sj]:
                    q.append((ni, nj))
                    colorless_visited[ni][nj] = 1
            else:
                if 0 <= ni < n and 0 <= nj < n and colorless_visited[ni][nj] == 0 and (arr[ni][nj] == "R" or arr[ni][nj] == "G"):
                    q.append((ni, nj))
                    colorless_visited[ni][nj] = 1
n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
colorless_visited = [[0] * n for _ in range(n)]
normal = 0
colorless = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            normal += 1
        if colorless_visited[i][j] == 0:
            colorless_bfs(i, j)
            colorless += 1
print(normal, colorless)
