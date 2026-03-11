import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited = [[-1] * m for _ in range(n)]
    visited[si][sj] = 0
    cnt = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == "L" and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                cnt = max(cnt, visited[ni][nj])
    return cnt
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dirs = [(0, 1),(0, -1),(1, 0),(-1, 0)]
tot = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            a = bfs(i, j)
            tot = max(tot, a)
print(tot)