import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    if arr[si][sj] == "-":
        while q:
            ci, cj = q.popleft()
            ni, nj = ci, cj + 1
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == "-" and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    elif arr[si][sj] == "|":
        while q:
            ci, cj = q.popleft()
            ni, nj = ci + 1, cj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == "|" and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
