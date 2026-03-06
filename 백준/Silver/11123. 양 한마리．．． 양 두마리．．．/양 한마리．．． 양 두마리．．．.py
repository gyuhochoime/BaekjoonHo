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
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == "#" and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
T = int(sys.stdin.readline())
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "#" and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    print(cnt)
