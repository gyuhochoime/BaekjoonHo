import sys
from collections import deque
def bfs(si):
    q = deque()
    q.append((0, si))
    visited[0][si] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
flag = False
for i in range(m):
    if arr[0][i] == 0 and visited[0][i] == 0:
        bfs(i)
for i in range(m):
    if visited[-1][i] == 1:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")