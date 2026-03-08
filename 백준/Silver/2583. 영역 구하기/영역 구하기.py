import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    res = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                res += 1
    return res
n, m, k = map(int, sys.stdin.readline().split())
arr = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ans = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(k):
    li, lj, ri, rj = map(int, sys.stdin.readline().split())
    for i in range(lj, rj):
        for j in range(li, ri):
            arr[i][j] = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visited[i][j] == 0:
            cnt = bfs(i, j)
            ans.append(cnt)
ans.sort()
print(len(ans))
print(*ans)
