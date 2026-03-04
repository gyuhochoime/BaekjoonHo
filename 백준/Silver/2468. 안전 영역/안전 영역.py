import sys
from collections import deque
def bfs(c):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > c and visited[i][j] == 0:
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > c and visited[ni][nj] == 0:
                            q.append((ni, nj))
                            visited[ni][nj] = 1
                cnt += 1
    return cnt
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
a = set()
for i in range(n):
    for j in range(n):
        a.add(arr[i][j])
safezone = []
for x in a:
    ans = bfs(x)
    safezone.append(ans)
if len(a) == 1:
    print(1)
else:
    print(max(safezone))
