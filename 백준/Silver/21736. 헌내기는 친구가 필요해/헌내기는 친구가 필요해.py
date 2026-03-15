import sys
from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
                if arr[ni][nj] == "O":
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                elif arr[ni][nj] == "P":
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1
    if cnt == 0:
        return "TT"
    else:
        return cnt    
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == "I":
            ans = bfs(i, j)
            print(ans)
            break
