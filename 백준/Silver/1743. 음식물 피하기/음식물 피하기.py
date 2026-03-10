import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                cnt += 1
    return cnt
n, m, k = map(int, sys.stdin.readline().split())
arr = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
food_trash = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    arr[r-1][c-1] = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ans = bfs(i, j)
            food_trash.append(ans)
print(max(food_trash))
