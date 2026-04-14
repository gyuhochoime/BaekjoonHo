import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 1 and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                if arr[ni][nj] != 0:
                    return visited[ni][nj]
    return -1
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
flag = False
ans = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            ans = bfs(i, j)
            flag = True
            break
    if flag:
        break
if ans == -1:
    print("NIE")
else:
    print("TAK")
    print(ans)