import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
tot = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            ans = bfs(i, j)
            tot.append(ans)
if len(tot) > 0:
    print(len(tot))
    print(max(tot))
else:
    print(0)
    print(0)
