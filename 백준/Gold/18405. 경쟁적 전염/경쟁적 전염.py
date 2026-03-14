import sys
from collections import deque
def bfs(num, si, sj, birus_a):
    q = deque()
    for a, b, c in birus_a:
        q.append((a, b, c))
    time = num
    while time > 0:
        for _ in range(len(q)):
            ci, cj, bi = q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append((ni, nj, bi))
                    visited[ni][nj] = bi
        time -= 1
    return visited[si-1][sj-1]
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())
visited = [[0] * n for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
birus = 1
tmp = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            tmp.append((i, j, arr[i][j]))
            visited[i][j] = arr[i][j]
tmp.sort(key = lambda x: x[2])
ans = bfs(s, x, y, tmp)
print(ans)
