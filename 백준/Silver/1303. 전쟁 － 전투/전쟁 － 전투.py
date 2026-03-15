import sys
from collections import deque
def w_bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == "W" and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt ** 2
def b_bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == "B" and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt ** 2
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
W = B = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            if arr[i][j] == "W":
                ans = w_bfs(i, j)
                W += ans
            elif arr[i][j] == "B":
                ans = b_bfs(i, j)
                B += ans
print(W, B)
