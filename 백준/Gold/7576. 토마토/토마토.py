import sys
from collections import deque
def bfs(t):
    a = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = -1
    while t:
        for _ in range(len(t)):
            ci, cj = t.popleft()
            for di, dj in a:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    t.append((ni, nj))
                    visited[ni][nj] = 1
        cnt += 1
    return cnt
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
flag = True
tomato = deque()
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            tomato.append((i, j))
            visited[i][j] = 1
ans = bfs(tomato)
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visited[i][j] == 0:
            flag = False
            break
    if not flag:
        break
if not flag:
    print(-1)
else:
    print(ans)
