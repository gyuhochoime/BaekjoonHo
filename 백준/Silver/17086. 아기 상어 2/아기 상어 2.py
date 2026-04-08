import sys
from collections import deque
def bfs():
    q = deque()
    for i, j in shark:
        q.append((i, j))
        visited[i][j] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    return max(map(max, visited))
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
shark = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            shark.append((i, j))
print(bfs())